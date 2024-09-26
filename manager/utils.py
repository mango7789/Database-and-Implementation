from .__init__ import *
from manager import models as mg_models
from django.db import transaction
from typing import Final

cost_to_goods: Final = 1.1

def load_json(json_path: str) -> dict:
    '''
    json_path: json文件的相对路径
    '''
    if json_path == None:
        raise FileNotFoundError
    with open(json_path, 'r', encoding="utf-8") as json_file:
        Json = json.load(json_file) 
    return Json

def random_image(images_dict: dict) -> list:
    '''
    images_dict: (验证码，图片位置)字典
    '''
    random.seed(int(time.time()))
    images_num = random.randint(1, 100)
    authen_code, img_path = images_dict[str(images_num)][0], "/static/captcha/" + images_dict[str(images_num)][1]
    image_ver = [authen_code, img_path]
    return image_ver

def database_dump(table: Model, file_path: str, Header: list[str]) -> None:
    """
    @table_name: 要导出的表，请注意传入的是Model类，即表本身，而不是表的名称
    @file_path: 导出的excel表格的相对路径，请注意，我们导出的大部分的文件都会放在static文件夹下
    @Header: 表头
    """
    data_qs = table.objects.all()
    data_frame = read_frame(qs=data_qs)
    data_frame.to_excel(file_path, index=False, header=Header if len(Header)>0 else True)
    return 

def send_info_to_mail(
        supplier: str,
        goods: str, 
        prev: float, 
        curr: float, 
        type: str = "order"
    ) -> None:
    # type = ["order", "cost"]
    text = '<b>' + supplier + "</b>供应的<b>" + goods + "</b>单价由原来的" + str(round(prev, 2)) + "元变为" + str(round(curr, 2)) + "元。"
    new_mail = mg_models.mail(text=text, type=1)
    new_mail.save()
    return

def transpose_list(original: list[list]) -> list[list]:
    '''
    将列表转置，用于list函数中`table_body`的生成
    '''
    
    # assert len(set([len(row) for row in original])) == 1, "请传入完整的数据！" # 用于开发过程测试
    transposed = list(map(list, zip(*original)))
    return transposed

@transaction.atomic # 由于要上传一整个文件，因此加了修饰器，把以下函数封装在一个事务中，防止写入数据库一半时断电等情况
def read_datafile(file_path: str):
    '''
    读入上传的文件，将其信息写入数据库，并返回错误信息
    当文件未写入时，total_len统一返回-1
    该函数封装在一个事务（transaction）中
    '''
    line_breaker = "<br>" # 用来换行
    file_type = file_path.split('.')[-1]
    if file_type == "csv":
        try:
            df = pandas.read_csv(file_path)
        except:
            return "", -1
    elif file_type in ["xlsx", "xls"]:
        try:
            df = pandas.read_excel(file_path)
        except:
            return "." + file_type + "文件中数据格式有误，请重新上传！", -1
    else:
        return "", -1
    column_names = df.columns.tolist()
    column_names = [col.strip() for col in column_names] # delete white space
    # check if the column name is the same
    if column_names != ["供应商名称", "商品名称", "商品订量", "金额", "门店名称"]:
        return "文件列名错误，请重新上传！", -1
    # check if the length of data rows is 0
    total_record_num = len(df)
    if total_record_num == 0:
        return "文件中不存在数据，请重新上传！", -1
    
    error_msg = ""

    ## 以下部分先对每一行进行检查，如果不违反外键约束，则将数据写入后端；
    ## 如果违反外键约束，则将错误信息返回，并且不写入任何数据，体现数据库transaction的思想

    supplier_name_set = set(mg_models.supplier.objects.values_list('name', flat=True))
    shop_name_set = set(mg_models.shop.objects.values_list('name', flat=True))

    correct = True
    error_msg_list = []
    error_msg_list.append('''<p style="color: purple; display:inline; font-weight: bold; font-size: 12px">字段要求：供应商名称（存在）、商品名称（长度不超过20）、商品订量（正整数）、金额（正数）、门店名称（存在）</p>''')
    for index, row in df.iterrows():
        supplier_name, goods_name, goods_order_num, cost_money, shop_name =  \
            row["供应商名称"], row["商品名称"], row["商品订量"], row["金额"], row["门店名称"]
        error = "第" + str(index+1) + "条数据存在错误，请检查以下字段："

        field = []
        flg = False

        if supplier_name not in supplier_name_set:
            correct = False
            flg = True
            # no_supplier = True
            field.append("供应商名称")
        else:
            field.append("…"*5)

        if len(goods_name) > 20 or not is_valid_string(str(goods_name)):
            correct = False
            flg = True
            field.append("商品名称")
        else:
            field.append("…"*4)

        try:
            goods_order_num = int(goods_order_num)
            if goods_order_num > 0 and goods_order_num == int(goods_order_num):
                field.append("…"*4)
            else:
                correct = False
                flg = True
                field.append("商品订量")
        except ValueError:
            correct = False
            flg = True
            field.append("商品订量")

        if (not isinstance(cost_money, int) and not isinstance(cost_money, float)) or cost_money<=0:
            correct = False
            flg = True
            field.append("金额")
        else:
            field.append("…"*2)

        if shop_name not in shop_name_set:
            correct = False
            flg = True
            # no_shop = True
            field.append("门店名称")
        else:
            field.append("…"*4)
        
        
        if flg:
            error = error + '，'.join(field)

            error_msg_list.append(error)
        
    if not correct:
        error_msg = line_breaker.join(error_msg_list)
        return error_msg, -1
        
    ## 如果没有错误，则向后端写入，以下部分基本复用manager模块下的views.py的order_add函数
    for index, row in df.iterrows():
        supplier_name, goods_name, goods_order_num, cost_money, shop_name =  \
            row["供应商名称"], row["商品名称"], row["商品订量"], row["金额"], row["门店名称"]
        
        ## 增加remian中的库存量，若不存在则创建，若存在则在原有数量上增加
        remain = mg_models.remain.objects.filter(shop_name=shop_name, goods_name=goods_name).values_list("goods_remain", flat=True)
        if not remain:
            mg_models.remain.objects.create(shop_name=shop_name, goods_name=goods_name, goods_remain=int(goods_order_num))
        else:
            mg_models.remain.objects.filter(shop_name=shop_name, goods_name=goods_name).update(goods_remain = int(remain[0]) + int(goods_order_num))

        ## 获取obj对象和当前进货单价
        goods_obj = mg_models.goods.objects.filter(name=goods_name)
        cost_obj = mg_models.cost.objects.filter(supplier_name=supplier_name, goods_name=goods_name)
        current_cost_unit = float(cost_money) / int(goods_order_num)
        ## 如果存在goods_obj，则cost_obj一定存在
        if goods_obj and cost_obj:
            cost_instance = cost_obj.first() 
            previous_cost_unit = cost_instance.cost_unit
            if current_cost_unit != previous_cost_unit:
                compare = 1 if current_cost_unit < previous_cost_unit else 3
                goods_obj.update(status="未确认")
                cost_obj.update(cost_unit=current_cost_unit, status="已进货", compare=compare)
                send_info_to_mail(cost_instance.supplier_name, cost_instance.goods_name, previous_cost_unit, current_cost_unit)
            
        # 不存在，则创建
        else:
            compare = 2
            sell_unit = round(cost_to_goods * current_cost_unit, 2)
            if not goods_obj:
                mail_text = "新建了<b>" + supplier_name + "</b>供应的<b>" + goods_name + "</b>单价信息，进货单价为" + str(current_cost_unit) + "元，请及时到商品单价界面查看！"
                if cost_obj:
                    compare = 1 if current_cost_unit < cost_obj.first().cost_unit else 3
                mg_models.mail.objects.create(type=2, text=mail_text)
                mg_models.goods.objects.create(type=1, name=goods_name, unit_sale=sell_unit, measurement="个")
                if cost_obj:
                    mg_models.cost.objects.filter(supplier_name=supplier_name, goods_name=goods_name).update(cost_unit=current_cost_unit, status="已进货", compare=compare) 
                else:
                    mg_models.cost.objects.create(supplier_name=supplier_name, goods_name=goods_name, cost_unit=current_cost_unit, status="已进货", compare=compare)

            ## goods存在，cost不存在
            else:
                mg_models.cost.objects.create(supplier_name=supplier_name, goods_name=goods_name, cost_unit=current_cost_unit, status="已进货")
                goods_obj.update(status="未确认")
                mail_text = "新建了<b>" + supplier_name + "</b>供应的<b>" + goods_name + "</b>单价信息，进货单价为" + str(current_cost_unit) + "元，请及时到商品单价界面查看！"
                mg_models.mail.objects.create(type=2, text=mail_text)
            ## 更新进货单价表
            
        ## 保存进货记录
        mg_models.order_record.objects.create(supplier_name=supplier_name,goods_name=goods_name,goods_order_num=goods_order_num,cost_money=cost_money,shop_name=shop_name)
    return "", total_record_num

    
def time_formatter(time):
    '''
    将时间格式化为年月日-时分秒的格式
    '''
    return time.strftime('%Y-%m-%d %H:%M:%S')

def clear_upload_files():
    '''
    当src文件夹下文件数多于60个时，清除其中的一半
    '''
    MAX_FILES = 60
    uploaded_files = os.listdir("./src/")

    if len(uploaded_files) > MAX_FILES:
        files_timestamp = sorted(uploaded_files)
        for k in range(int(MAX_FILES/2)):
            os.remove("./src/" + files_timestamp[k])

def is_valid_string(s) -> bool:
    return bool(match(r'^[a-zA-Z\u4e00-\u9fff]+$', s))