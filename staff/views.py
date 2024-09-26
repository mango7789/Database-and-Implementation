from staff import models
from manager import models as mg_models
from .__init__ import *
from manager.utils import transpose_list
from typing import Final
from django.db import transaction


choice_type: Final = dict(mg_models.goods.type_choice) # 商品类别

button_style: Final = '''style="padding: 0px 8px; font-size: 12px; margin-top: 0px"'''
list_sell_html: Final = \
        '''
        <a class="btn btn-round btn-warning" ''' + button_style + ''' href="/staff/sale/{}/add/">售出</a>
        ''' 

def session_check(key):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.session[key] == 'staff':
                return func(request, *args, **kwargs)
            else:
                return render(request, 'page_403.html', status=403)

        return wrapper
    return decorator


def float_right_align(price):
    """
    将价格浮点数右对齐
    """
    padding =  "{:+>8}".format(str(price))
    padding = padding.replace('+', '&nbsp;&nbsp;')
    return padding

@session_check("per")
def help(request):
    return render(request, "staff_help.html")

######################################################################
#                            shop info                               #
######################################################################

@session_check("per")
def staff_shop_list(request):
    """
    如果q是空字符串，则展示所有门店信息；
    否则查询对应商品仍然有余量的门店
    """
    nid = request.session.get("shop_id")
    shop_name = mg_models.shop.objects.filter(id=nid).values_list('name', flat=True)[0]
    current_shop_name = shop_name
    value = request.GET.get('q', "")
    # 如果传了参数q，则把名称满足查询条件、且库存量大于0的商品以及所在商店信息返回
    if value:
        table_header = ["编号", "商店名称", "地址", "联系电话", "负责人","余量"] 
        remain_list = mg_models.remain.objects.filter(goods_name__icontains=value).filter(goods_remain__gt=0).values_list('shop_name', 'goods_remain','goods_name')
        data_list = []
        for i in range(len(remain_list)):
            shop_name, remain_num, goods_name = remain_list[i][0], remain_list[i][1], remain_list[i][2]
            shop_obj = mg_models.shop.objects.filter(name=shop_name).first()
            goods_obj = mg_models.goods.objects.filter(name=goods_name,status="已确认").first()
            if shop_obj is not None and goods_obj is not None:
                shop_obj.goods_remain = remain_num
                data_list.append(shop_obj)
        table_body = [
            [obj.id for obj in data_list],
            ["<b>" + obj.name + "</b>" if obj.name == shop_name else obj.name for obj in data_list],
            ["".join(obj.location.split("-")) + obj.location_specific for obj in data_list],
            [obj.telephone for obj in data_list],
            [obj.salesman_name for obj in data_list],
            [obj.goods_remain for obj in data_list],
        ]
        table_body = transpose_list(table_body)
        return render(request, "_staff_ls.html", {
            "table_header": table_header, "table_body":table_body, 
            "list_name": "门店信息表", "people_name": request.session.get('name'),
            "shop_name": current_shop_name, "goods_name":value
        })
        
    # 如果没有传参数q，就把所有店铺信息全部返回
    else: 
        data_list = mg_models.shop.objects.filter()
        table_header = ["编号", "商店名称", "地址", "联系电话", "负责人"] 
        table_body = [
            [obj.id for obj in data_list],
            ["<b>" + obj.name + "</b>" if obj.name == shop_name else obj.name for obj in data_list],
            ["".join(obj.location.split("-")) + obj.location_specific for obj in data_list],
            [obj.telephone for obj in data_list],
            [obj.salesman_name for obj in data_list],
        ]
        table_body = transpose_list(table_body)
        return render(request, "_staff_ls.html", {
            "table_header": table_header, "table_body":table_body,
            "list_name": "商店信息表", "people_name": request.session.get('name'),
            "shop_name": shop_name, "goods_name": value
        })


######################################################################
#                          remain & sell                             #
######################################################################

@session_check("per")
def staff_goods_list(request):
    """
    如果q是空字符串，则返回本店库存量大于0的商品信息；
    如果q不是空字符串，则检索包含该字符串且库存量大于0的商品信息
    """
    nid = request.session.get("shop_id")
    shop_name = mg_models.shop.objects.filter(id=nid).values_list('name', flat=True)[0]
    value = request.GET.get('q', "")
    if value:  # 返回本店中名称包含该字段的商品余量信息
        remain_list = mg_models.remain.objects.filter(shop_name=shop_name, goods_name__icontains=value).filter(goods_remain__gt=0)
    else:  # 如果没有传参数q，就全部返回所有商品的余量信息
        remain_list = mg_models.remain.objects.filter(shop_name=shop_name).filter(goods_remain__gt=0)
    
    data_list = []
    # 查询本店满足查询条件且余量大于0的商品的其他相关信息
    for remain_obj in remain_list: 
        goods_obj = mg_models.goods.objects.filter(name=remain_obj.goods_name).first() # 把商品的其他信息也查询出来
        goods_obj.goods_remain = remain_obj.goods_remain
        goods_status = goods_obj.status
        if goods_status == "未确认":
            continue
        data_list.append(goods_obj)
    table_header = ["商品名","商品类别","销售单价","计量单位","商品余量","操作"] 
    table_body = [
        [obj.name for obj in data_list],
        [choice_type[obj.type] for obj in data_list],
        [float_right_align(obj.unit_sale) for obj in data_list],
        [obj.measurement for obj in data_list],
        [obj.goods_remain for obj in data_list],
        [list_sell_html.format(obj.id) for obj in data_list],
    ]
    table_body = transpose_list(table_body)
    return render(request, "_staff_ls.html", {
        "table_header": table_header, "table_body":table_body,
        "list_name": "商品库存表", "people_name": request.session.get('name'),
        "shop_name": shop_name, "goods_name":value
    })

# 销售记录表单
class saleform(forms.ModelForm):
    goods_name = forms.CharField(max_length=20, label="商品名称", required=False, disabled=True)
    goods_sale_num = forms.IntegerField(label="销售数量", required=True)
    goods_type = forms.CharField(label="类别", required=False, disabled=True)
    measurement = forms.CharField(label="计量单位", required=False, disabled=True)
    remain = forms.IntegerField(label="余量", required=False, disabled=True)
    sale_price = forms.CharField(label="销售单价", required=False, disabled=True)

    class Meta:
        model = mg_models.remain
        fields = ['goods_name', 'goods_sale_num', 'goods_type', 'measurement', 'remain', 'sale_price']
    field_order = ['goods_name', 'goods_type', 'sale_price', 'measurement', 'remain', 'goods_sale_num']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    def clean_goods_sale_num(self):
        sale_num = self.cleaned_data['goods_sale_num']
        remain = self.cleaned_data['remain']
        try:
            sale_num, remain = map(int, [sale_num, remain])
        except:
            raise ValidationError("请输入有效的销售数量！")
        if sale_num > remain:
            raise ValidationError("销售量大于库存量，无法售出！")
        elif sale_num < 0:
            raise ValidationError("请输入有效的销售数量！")
        return sale_num

@session_check("per")
@transaction.atomic
def staff_sale_receipt_add(request, nid):  
    """
    卖出一种商品，自动增加一条销售记录

    Args:
    - nid: 商品在goods表中的nid，通过URL传递
    """

    goods_obj = mg_models.goods.objects.filter(id=nid).first()
    shop_id = request.session.get("shop_id")
    shop_name = mg_models.shop.objects.filter(id=shop_id).values_list('name', flat=True)[0]
    remain = mg_models.remain.objects.filter(shop_name=shop_name, goods_name=goods_obj.name).first()
    initial_data = {
        "goods_name": goods_obj.name, "goods_type": choice_type[goods_obj.type], 
        "measurement": goods_obj.measurement, "remain": remain.goods_remain, 
        'sale_price':goods_obj.unit_sale
    }
    if request.method == "GET":
        form = saleform(initial=initial_data)
        return render(request, '_staff_fm.html', {"form": form, "form_name": "售出商品","people_name": request.session.get('name'), "shop_name": shop_name})
    
    form = saleform(data=request.POST, initial=initial_data)
    if form.is_valid():
        goods_sale_num = request.POST.get("goods_sale_num")
        sale_price = mg_models.goods.objects.filter(name=goods_obj.name).values_list("unit_sale", flat=True)[0]
        remain= mg_models.remain.objects.filter(shop_name=shop_name, goods_name=goods_obj.name).values_list("goods_remain", flat=True).first()
        
        turnover = int(goods_sale_num) * float(sale_price)
        mg_models.remain.objects.filter(shop_name=shop_name, goods_name=goods_obj.name).update(goods_remain=int(remain)-int(goods_sale_num))
        mg_models.sale_record.objects.create(shop_name=shop_name, goods_name=goods_obj.name, goods_sale_num=goods_sale_num, turnover=turnover, sale_man_id=request.session.get("id"))
        
        return redirect("/staff/goods/list")  # 转到本店的销售历史记录
    form = saleform(data=request.POST, initial=initial_data)
    return render(request, '_staff_fm.html', {"form": form, "form_name": "售出商品", "people_name": request.session.get('name'), "shop_name":shop_name})


######################################################################
#                          sales history                             #
######################################################################

@session_check("per")
def staff_sale_list(request):
    """展示本店的销售历史记录""" 
    nid = request.session.get("shop_id")
    name = mg_models.shop.objects.filter(id=nid).values_list('name', flat=True)[0]
    value = request.GET.get('q', "")
    data_list = mg_models.sale_record.objects.filter(shop_name=name, goods_name__icontains=value).order_by('-sale_time')
    table_header = ["编号", "商品名", "售出量","毛利", "销售时间"] 
    table_body = [
        [i+1 for i in range(len(data_list))],
        [obj.goods_name for obj in data_list],
        [obj.goods_sale_num for obj in data_list],
        [float_right_align(obj.turnover) for obj in data_list],
        [obj.sale_time.strftime('%Y-%m-%d %H:%M:%S') for obj in data_list],
    ]
    table_body = transpose_list(table_body)
    return render(request, "_staff_ls.html", {
        "table_header": table_header, "table_body": table_body,
        "list_name": "本店销售记录", "people_name": request.session.get("name"), 
        "shop_name": name, "goods_name": value
    })
