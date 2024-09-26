from manager import models
from staff import models as models_s
from .forms import *
from .__init__ import *
from .utils import *
from .config import *

######################################################################
#                              admin                                 #
######################################################################

def session_check(key):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if key == 'per':
                if request.session.get(key) == 'manager':
                    return func(request, *args, **kwargs)
                else:
                    return render(request, 'page_403.html', status=403)
            elif key == 'id':
                return func(request, *args, **kwargs)
            return render(request, 'page_403.html', status=403)
        return wrapper
    return decorator

def admin(request):
    pass

def log_out(request):
    logout(request)
    del request.session
    return redirect('/')

######################################################################
#                             log in                                 #
######################################################################

def log_in(request):
    """登陆界面"""
    try:
        del request.session['id']
        del request.session['name']
        del request.session['per']
    except:
        pass
    global image_ver
    if request.method == "GET":
        form = loginform()
        image_ver = random_image(AUTHEN_IMAGES)
        return render(request, 'log_in.html', {'id': "", "type": 1, "src": image_ver[1]})
    
    if image_ver[1] == None:
        image_ver = random_image(AUTHEN_IMAGES)

    form = loginform(data=request.POST)

    fields = ["type", "id", "password", "vercode"]
    type, id, pwd, ver_code = map(request.POST.get, fields)
    type = int(type)
    if form.is_valid():
        # type == 1 时登录管理层页面
        if type == 1:
            obj = models.manager.objects.filter(id=id, password=pwd).first()
            if obj:
                # if ver_code.lower() == image_ver[0].lower():
                try:
                    del request.session["shop_id"]
                except:
                    pass
                request.session['id'], request.session['name'], request.session['per'] = id, obj.name, 'manager'
                return redirect("/homepage") 
        # type == 2 时登录员工页面
        elif type == 2:
            obj = models_s.salesman.objects.filter(id=id, salesman_password=pwd).first()
            if obj:
                # NOTE: you can switch on/off the check of authentication code here
                # if ver_code.lower() == image_ver[0].lower():
                request.session['id'], request.session['name'], request.session['shop_id'], request.session['per'] \
                    = id, obj.salesman_name, obj.shop_id.id, 'staff'
                return redirect("/staff/shop/list")
        else:
            pass
    if id == "" or pwd == "":
        error_msg = "请输入ID和密码！"
    elif ver_code == "":
        error_msg = "请输入验证码！"
    else:
        error_msg = "密码或验证码错误，登录失败！"

    return render(request, 'log_in.html', {'error_msg': error_msg, "id": id, "type": type, "src": image_ver[1]})


###################################################################### 
#                            homepage                                #
######################################################################

@session_check("per")
def homepage(request):
    """主页"""
    ## calculate the total numbers of the objects, which correspond to the first row of homepage
    shop_query_set = models.shop.objects.filter()
    shop_total = len(shop_query_set)
    user_total = len(models_s.salesman.objects.filter())
    supplier_total = len(models.supplier.objects.filter())
    goods_total = len(models.goods.objects.filter())
    mail_total = len(models.mail.objects.filter())
    
    ## now focus on the sale and order data, first we get the queryset of them
    sale_query_set = models.sale_record.objects.filter() 
    order_query_set = models.order_record.objects.filter()
    sale_total = 0                      # total sales
    order_total = 0                     # total_order
    current_time = datetime.now()    # current time, just need to fetch once
    datetime_weekday_convert = {        # converter
        0: "星期一",
        1: "星期二",
        2: "星期三",
        3: "星期四",
        4: "星期五",
        5: "星期六",
        6: "星期日"
    }
    ## init these dicts for storing data 
    # chart 1
    quarter_xaxis = [
        "{}~{}".
        format((current_time - timedelta(days=7*n)).strftime("%m.%d"), 
                (current_time - timedelta(days=7*(n-1))).strftime("%m.%d")) for n in range(12, 0, -1)
    ]
    quarter_sale = {
        quarter_xaxis[i]: {"sale_data": 0, "pure_data": 0} for i in range(len(quarter_xaxis))
    }
    # chart 2
    shop_sale = {
        obj.name: {"sale_data": 0, "pure_data": 0} for obj in shop_query_set
    }
    # chart 3
    provinces_list = ["河北", "山西", "辽宁", "吉林", "黑龙江", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "海南", "四川", "贵州", "云南", "陕西", "甘肃", "青海", "台湾", "内蒙古", "广西", "西藏", "宁夏", "新疆", "北京", "天津", "上海", "重庆", "香港", "澳门", "南海诸岛"]
    map_sale = {
        name: 0 for name in provinces_list
    }
    self_admin_converter = {
        "新疆维吾尔": "新疆",
        "内蒙古": "内蒙古",
        "宁夏回族": "宁夏",
        "广西壮族": "广西",
        "西藏": "西藏",
    }
    # chart 4
    type_sale = {
        CHOICE_TYPE[i]: 0 for i in range(1, 6)
    }
    
    # chart 5
    weekday_sale = {
        value: {"sale_data": 0, "order_data": 0, "pure_data": 0} for _, value in datetime_weekday_convert.items()
    }
    # chart 6
    revenue_rate = lambda pure_data, sale_data: round(pure_data / sale_data, 2)

    ## iterate the query sets
    # first we iterate the sale_record query set
    for sale_obj in sale_query_set:
        sale_shop, sale_goods, sale_money, sale_time = \
            sale_obj.shop_name, sale_obj.goods_name, float(sale_obj.turnover), sale_obj.sale_time
        # chart 1
        for k in range(1, 13):
            transformed_time = sale_time + timedelta(days=7*k)
            if transformed_time >= current_time and k != 12:
                quarter_sale[quarter_xaxis[12-k]]['sale_data'] += sale_money
                quarter_sale[quarter_xaxis[12-k]]['pure_data'] += sale_money
                break
            elif transformed_time == current_time and k == 12:
                quarter_sale[0]['sale_data'] += sale_money
                quarter_sale[0]['pure_data'] += sale_money
                break
        # chart 2
        if current_time - timedelta(days=84) < sale_time:
            shop_sale[sale_shop]['sale_data'] += sale_money 
            shop_sale[sale_shop]['pure_data'] += sale_money    
        # chart 3
        shop_site = str(models.shop.objects.filter(name=sale_shop).first().location)
        check_direct = shop_site[0:2] in ["北京", "天津", "上海", "重庆"]
        if check_direct:
            province_name = shop_site.split("市")[0] 
        elif len(shop_site.split('自治区')) > 1:
            province_name = self_admin_converter[shop_site.split('自治区')[0]]
        else:
            province_name = shop_site.split("省")[0]
        map_sale[province_name] += sale_money
        # chart 4
        sale_goods_type = models.goods.objects.filter(name=sale_goods).first().type
        type_sale[CHOICE_TYPE[sale_goods_type]] += sale_money
        # chart 5
        sale_weekday = sale_time.weekday()
        weekday_sale[datetime_weekday_convert[sale_weekday]]['sale_data'] += sale_money
        weekday_sale[datetime_weekday_convert[sale_weekday]]['pure_data'] += sale_money
        # chart 6
        sale_total += sale_money
    
    # now we iterate the order_record query set
    for order_obj in order_query_set:
        order_shop, order_goods, order_money, order_time = \
            order_obj.shop_name, order_obj.goods_name, float(order_obj.cost_money), order_obj.order_time
        # chart 1
        for k in range(1, 13):
            transformed_time = order_time + timedelta(days=7*k)
            if transformed_time >= current_time and k != 12:
                quarter_sale[quarter_xaxis[12-k]]['pure_data'] -= order_money
                break
            elif transformed_time == current_time and k == 12:
                quarter_sale[0]['pure_data'] -= order_money
                break
        # chart 2
        if current_time - timedelta(days=84) < order_time:
            shop_sale[order_shop]['pure_data'] -= order_money   
        # chart 3 and 4 are only for sale_data
    
        # chart 5
        order_weekday = order_time.weekday()
        weekday_sale[datetime_weekday_convert[order_weekday]]['pure_data'] -= order_money
        weekday_sale[datetime_weekday_convert[order_weekday]]['order_data'] += order_money
        # chart 6
        order_total += order_money

    if sale_total == 0.:
        gauge_rate = 0
    else:
        gauge_rate = round(max(0, revenue_rate(sale_total-order_total, sale_total)) * 100, 2)

    ## formulate these dicts
    # chart 1
    bar_one_data = {
        "xaxis": quarter_xaxis,
        "sale_data": [round(value['sale_data'], 2) for key, value in quarter_sale.items()],
        "pure_data": [round(value['pure_data'], 2) for key, value in quarter_sale.items()],
    }
    # chart 2
    sorted_shop_sale = sorted(shop_sale.items(), key=lambda x: (x[1]["sale_data"], x[1]["pure_data"]), reverse=True)
    valid_sorted_shop_sale = min(len(sorted_shop_sale), 5)
    shop_sale_dict = {
        sorted_shop_sale[valid_sorted_shop_sale - i][0]: sorted_shop_sale[valid_sorted_shop_sale - i][1] for i in range(valid_sorted_shop_sale) 
    }
    bar_hrz_data = {
        "yaxis": list(shop_sale_dict.keys()),
        "sale_data": [round(value['sale_data'], 2) for _, value in shop_sale_dict.items()],
        "pure_data": [round(value['pure_data'], 2) for _, value in shop_sale_dict.items()],
    }
    # chart 3
    map_data = {
        "min_value": round(min(map_sale.values()), 1),
        "max_value": round(max(map_sale.values()), 1),
        "sale_data": [{"name": name, "value": round(value, 1)} for name, value in map_sale.items()]
    }
    # chart 4
    donut_data = {
        "type_name": list(CHOICE_TYPE.values()),
        "pie_data": [{"value": round(value, 2), "name": key} for key, value in type_sale.items()]
    }
    # chart 5
    line_data = {
        "pure_data": [round(value['pure_data'], 2) for _, value in weekday_sale.items()],
        "order_data": [round(value['order_data'], 2) for _, value in weekday_sale.items()],
        "sale_data": [round(value['sale_data'], 2) for _, value in weekday_sale.items()],
    }

    data_dict = {
        "shop_total": shop_total,
        "user_total": user_total,
        "supplier_total": supplier_total,
        "goods_total": goods_total,
        "sale_total": round(sale_total, 1),
        "mail_total": mail_total,
        "bar_one_data": bar_one_data,
        "bar_hrz_data": bar_hrz_data,
        "map_data": map_data,
        "donut_data": donut_data,
        "line_data": line_data,
        "gauge_rate": gauge_rate,
        "people_name": request.session.get('name'),
    }

    return render(request, '_homepage.html', data_dict)

@session_check("id")
def help(request):
    """
    帮助文档，在界面的右上角
    """
    # if request.session["shop_id"] is not None:
    #     return render(request, "staff_help.html")
    try:
        shop_id = request.session["shop_id"]
        return render(request, "staff_help.html")
    except:
        return render(request, "manager_help.html")

###################################################################### 
#                              shop                                  #
######################################################################

@session_check("per")
def shop_list(request):
    """展示门店信息"""
    data_list = models.shop.objects.filter()
    table_header = ["编号", "商店名称", "地址", "联系电话", "负责人", "操作"] 
    table_body = [
        [obj.id for obj in data_list],
        [obj.name for obj in data_list],
        ["".join(obj.location.split("-")) + obj.location_specific for obj in data_list],
        [obj.telephone for obj in data_list],
        [obj.salesman_name for obj in data_list],
        [str(LIST_MODIFY_BUTTON + LIST_REDIRECT_BUTTON).format(obj.id, obj.id) for obj in data_list],
    ]
    table_body = transpose_list(table_body)
    return render(request, "_list.html", {"table_header": table_header, "table_body":table_body, "list_name": "门店信息表", "people_name": request.session.get('name')})

@session_check("per")
def shop_add(request):
    """增加门店"""
    if request.method == "GET":
        form = shopform()
        return render(request, "_form.html", {"form": form, "form_name": "添加门店", "people_name": request.session.get('name')})
    form = shopform(data=request.POST)
    if form.is_valid():
        form.save(commit=False)
        name, location, telephone, salesman_name = form.cleaned_data['name'], form.cleaned_data['province'] + '-' + form.cleaned_data['city'], form.cleaned_data['telephone'], form.cleaned_data['salesman_name']
        location_spec = form.cleaned_data['location']
        models.shop.objects.create(name=name, location=location, telephone=telephone, salesman_name=salesman_name, location_specific=location_spec)
        return redirect("/shop/list")
    return render(request, '_form.html', {"form": form, "form_name": "添加门店", "people_name": request.session.get('name')})

@session_check("per")
def shop_modify(request, nid):
    """修改门店信息"""
    obj = models.shop.objects.filter(id=nid).first()
    initial_data = {
        "previous": "".join(obj.location.split("-")) + obj.location_specific
    }
    if request.method == "GET":
        form = shopform_modify(instance=obj, initial=initial_data)
        return render(request, '_form.html', {"form": form, "form_name": "修改门店信息", "people_name": request.session.get('name')})
    form = shopform_modify(data=request.POST, instance=obj, initial=initial_data)
    if form.is_valid():
        form.save(commit=False)
        name, telephone, salesman_name = form.cleaned_data['name'], form.cleaned_data['telephone'], form.cleaned_data['salesman_name']
        location_spec = form.cleaned_data['location_specific']
        models.shop.objects.filter(id=nid).update(name=name, telephone=telephone, salesman_name=salesman_name, location_specific=location_spec)
        return redirect("/shop/list")
    return render(request, '_form.html', {"form": form, "form_name": "修改门店信息", "people_name": request.session.get('name')})

@session_check("per")
def shop_salesman(request, nid):
    """展示某个门店的店员信息"""
    if nid == 0:
        data_list = models_s.salesman.objects.filter()
        shop_name = ""
        table_header = ["员工编号", "所属商店", "名称", "密码", "操作"]
        table_body = [
            [obj.id for obj in data_list],
            [obj.shop_id.name for obj in data_list],
            [obj.salesman_name for obj in data_list],
            [obj.salesman_password for obj in data_list],
            [str(LIST_MODIFY_BUTTON + LIST_DELETE_BUTTON).format(obj.id, obj.id) for obj in data_list],
        ]
    else:
        data_list = models_s.salesman.objects.filter(shop_id=nid)
        # 传入该门店的名称
        shop_name = models.shop.objects.filter(id=nid).first().name
        table_header = ["员工编号", "名称", "密码"]
        table_body = [
            [obj.id for obj in data_list],
            [obj.salesman_name for obj in data_list],
            [obj.salesman_password for obj in data_list],
        ]
    table_body = transpose_list(table_body)
    return render(request, "_list.html", {"table_header": table_header, "table_body":table_body, "list_name": shop_name + "员工信息表", "people_name": request.session.get('name')})

@session_check("per")
def shop_salesman_add(request, nid):
    """为某个门店增加店员"""
    if request.method == "GET":
        if nid == 0:
            form = salesmanform()
        else:
            form = salesmanform({"shop_name": models.shop.objects.get(id=nid).name})
            form.fields['shop_name'].widget.attrs['readonly'] = True
        return render(request, '_form.html', {"form": form, "form_name": "添加员工信息", "people_name": request.session.get('name')})
    form = salesmanform(data=request.POST)
    if form.is_valid():
        partial_instance = form.save(commit=False)
        if nid == 0:
            partial_instance.shop_id = models.shop.objects.get(name=form.cleaned_data['shop_name'])
        else:
            current_shop_instance = models.shop.objects.get(id=nid)
            partial_instance.shop_id = current_shop_instance
        partial_instance.save()
        return redirect("/shop/{0}/salesman".format(nid))
    return render(request, '_form.html', {"form": form, "form_name": "添加员工信息", "people_name": request.session.get('name')})
        
@session_check("per")
def shop_salesman_modify(request, nid):
    """修改某个门店的某个店员的个人信息"""
    obj = models_s.salesman.objects.filter(id=nid).first()
    if request.method == "GET":
        form = salesmanmodifyform(instance=obj, initial={"shop_name": obj.shop_id.name})
        return render(request, '_form.html', {"form": form, "form_name": "修改员工信息", "people_name": request.session.get('name')})
    form = salesmanmodifyform(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/shop/0/salesman/")
    form = salesmanmodifyform(instance=obj, initial={"shop_name": obj.shop_id.name}, data=request.POST)
    return render(request, '_form.html', {"form": form, "form_name": "修改员工信息", "people_name": request.session.get('name')})

@session_check("per")
def shop_salesman_delete(request, nid):
    """删除某个门店的某个店员"""
    obj = models_s.salesman.objects.filter(id=nid).first()
    obj.delete()
    return redirect("/shop/0/salesman/")


######################################################################
#                             supplier                               #
######################################################################

@session_check("per")
def supplier_list(request):
    """展示所有供应商的信息"""
    data_list = models.supplier.objects.filter()
    table_header = ["供应商编号", "供应商名称", "联系电话", "邮箱", "操作"]
    table_body = [
        [obj.id for obj in data_list],
        [obj.name for obj in data_list],
        [obj.telephone for obj in data_list],
        [obj.email for obj in data_list],
        [LIST_MODIFY_BUTTON.format(obj.id) for obj in data_list],
    ]
    table_body = transpose_list(table_body)
    return render(request, "_list.html", {"table_header": table_header, "table_body":table_body, "list_name": "供应商信息表", "people_name": request.session.get('name')})

@session_check("per")
def supplier_add(request):
    """添加一个供应商"""
    if request.method == "GET":
        form = supplierform()
        return render(request, "_form.html", {"form": form, "form_name": "添加供应商", "people_name": request.session.get('name')})
    form = supplierform(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/supplier/list")
    return render(request, "_form.html", {"form": form, "form_name": "添加供应商", "people_name": request.session.get('name')})

@session_check("per")
def supplier_modify(request, nid):
    """修改某个供应商的信息"""
    obj = models.supplier.objects.filter(id=nid).first()
    if request.method == "GET":
        form = supplierform_modify(instance=obj)
        return render(request, '_form.html', {"form": form, "form_name": "修改供应商信息", "people_name": request.session.get('name')})
    form = supplierform_modify(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/supplier/list")
    return render(request, '_form.html', {"form": form, "form_name": "修改供应商信息", "people_name": request.session.get('name')})


######################################################################
#                              goods                                 #
######################################################################

def float_right_align(price):
    """
    将列表中浮点数右对齐，更加美观
    """
    padding =  "{:+>10}".format(str(price))
    padding = padding.replace('+', '&nbsp;&nbsp;')
    return padding

def calculate_cost_unit(obj):
    '''
    计算商品平均进货单价
    '''
    true_order = models.order_record.objects.filter(goods_name=obj.name)
    if true_order:
        return round(sum([obj.cost_money for obj in true_order]) / sum([obj.goods_order_num for obj in true_order]), 2)
    return 0.

def compare_then_arrow(cost_unit, obj, threshold=1.5):
    '''
    将进货单价与售价比较，并用箭头提示
    '''
    if cost_unit > obj.unit_sale:
        return float_right_align(obj.unit_sale) + ARROW_DOWN_RED
    elif threshold * float(cost_unit) < obj.unit_sale:
        return float_right_align(obj.unit_sale) + ARROW_UP_ORANGE
    return float_right_align(obj.unit_sale)

@session_check("per")
def goods_list(request):
    """展示所有商品的信息"""
    data_list = models.goods.objects.filter()
    table_unit_sale = [calculate_cost_unit(obj) for obj in data_list]
    table_header = ["商品编号",  "商品名称", "商品类型", "进货平均单价", "销售单价", "计量单位", "状态", "操作"]
    table_body = [
        [obj.id for obj in data_list],
        [obj.name for obj in data_list],
        [CHOICE_TYPE[obj.type] for obj in data_list],
        [float_right_align(cost_unit) for cost_unit in table_unit_sale],
        [compare_then_arrow(table_unit_sale[i], obj) for i, obj in enumerate(data_list)],
        [obj.measurement for obj in data_list],
        [SPAN_SUCCESS.format(obj.status) if obj.status=="已确认" else SPAN_DANGER.format(obj.status) for obj in data_list],
        [LIST_MODIFY_BUTTON.format(obj.id) for obj in data_list],
    ]
    table_body = transpose_list(table_body)
    return render(request, "_list.html", {"table_header": table_header, "table_body": table_body, "list_name": "商品信息表", "people_name": request.session.get('name')})

@session_check("per")
@transaction.atomic
def goods_modify(request, nid):
    """修改某件商品的信息"""
    obj = models.goods.objects.filter(id=nid).first()
    cost_ave = calculate_cost_unit(obj)
    if request.method == "GET":
        form = goodsform_modify(instance=obj, initial={"order_unit": cost_ave})
        return render(request, '_form.html', {"form": form, "form_name": "修改商品信息", "people_name": request.session.get('name')})
    form = goodsform_modify(data=request.POST, instance=obj)
    if form.is_valid():
        modified_data = form.cleaned_data
        mail_text = "商品名称为<b>" + str(obj.name) + "</b>的商品信息发生了改动！"
        models.mail.objects.create(type=3, text=mail_text)
        models.goods.objects.filter(id=nid).update(status="已确认", 
                                                   type=modified_data['type'], unit_sale=modified_data['unit_sale'],
                                                   measurement=modified_data['measurement']
                                                   )
        return redirect("/goods/list")
    form = goodsform_modify(instance=obj, initial={"order_unit": cost_ave}, data=request.POST)
    return render(request, '_form.html', {"form": form, "form_name": "修改商品信息", "people_name": request.session.get('name')})


######################################################################
#                               cost                                 #
######################################################################

def cost_unit_arrow(obj):
    """
    将目前进货单价与上一次进货单价比较，并加入对应的上/下箭头信息
    """
    if obj.compare == 1:
        return float_right_align(str(obj.cost_unit)) + ARROW_DOWN_GREEN
    elif obj.compare == 3:
        return float_right_align(str(obj.cost_unit)) + ARROW_UP_RED
    return float_right_align(str(obj.cost_unit))

@session_check("per")
def cost_list(request):
    """展示所有商品的进货单价"""
    data_list = models.cost.objects.filter()
    table_header = ["编号", "供应商", "商品名", "进货单价", "状态", "操作"] 
    table_body = [
        [obj.id for obj in data_list],
        [obj.supplier_name for obj in data_list],
        [obj.goods_name for obj in data_list],
        [cost_unit_arrow(obj) for obj in data_list],
        [SPAN_WARNING.format(obj.status) if obj.status == "预订购" else SPAN_SUCCESS.format(obj.status) for obj in data_list],
        [LIST_MODIFY_BUTTON.format(obj.id) for obj in data_list],
    ]
    table_body = transpose_list(table_body)
    return render(request, "_list.html", {"table_header": table_header, "table_body": table_body, "list_name": "进货单价表", "people_name": request.session.get('name')})

@session_check("per")
def cost_add(request):
    """
    修改某件商品的进货单价
    请注意，这里是手动添加；在order模块下，也可以通过后端自动添加
    """
    if request.method == "GET":
        form = cost_form()
        return render(request, "_form.html", {"form": form, "form_name": "添加进货单价信息", "people_name": request.session.get('name')})
    form = cost_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/cost/list")
    return render(request, '_form.html', {"form": form, "form_name": "添加进货单价信息", "people_name": request.session.get('name')})

@session_check("per")
@transaction.atomic
def cost_modify(request, nid):
    """
    修改某件商品的进货单价
    请注意，这里是手动修改；在order模块下，也可以通过后端自动修改
    """
    obj = models.cost.objects.filter(id=nid).first()
    prev_cost_unit = obj.cost_unit
    if request.method == "GET":
        form = costform_modify(instance=obj)
        return render(request, '_form.html', {"form": form, "form_name":"修改进货单价信息", "people_name": request.session.get('name')})
    form = costform_modify(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        curr_cost_unit = round(float(request.POST.get("cost_unit")), 2)
        curr_cost_unit, prev_cost_unit = round(curr_cost_unit, 2), round(prev_cost_unit, 2)
        if float(curr_cost_unit) != float(prev_cost_unit):
            compare = 1 if curr_cost_unit < prev_cost_unit else 3
            models.cost.objects.filter(id=nid).update(compare=compare, status="预订购")
            send_info_to_mail(obj.supplier_name, obj.goods_name, prev_cost_unit, curr_cost_unit, "cost")
        else:
            models.cost.objects.filter(id=nid).update(compare=2, status="预订购")
        return redirect("/cost/list")
    return render(request, '_form.html', {"form": form, "form_name":"修改进货单价信息", "people_name": request.session.get('name')})


######################################################################
#                               order                                #
######################################################################

@session_check("per")
def order_list(request):
    """
    展示所有进货记录
    请注意，进货是一个三元关系，从哪个供应商进货，进了什么商品，送到哪个店铺
    """
    data_list = models.order_record.objects.filter()
    total_len = len(data_list)
    table_header = ["编号", "供应商名称", "商品名称", "进货数量", "支付金额", "进货商店名称", "时间"] 
    table_body = [
        [total_len - obj.id + 1 for obj in data_list],
        [obj.supplier_name for obj in data_list],
        [obj.goods_name for obj in data_list],
        [obj.goods_order_num for obj in data_list],
        [float_right_align(obj.cost_money) for obj in data_list],
        [obj.shop_name for obj in data_list],
        [obj.order_time.strftime('%Y-%m-%d %H:%M:%S') for obj in data_list],
    ]
    table_body = transpose_list(table_body)
    return render(request, "_list.html", {"table_header": table_header, "table_body":table_body, "list_name": "进货记录表", "people_name": request.session.get('name')})

@session_check("per")
@transaction.atomic
def order_add(request):
    """手动增加一条进货记录；如果不存在某件商品，则会在goods，cost和remain中添加，并向收件箱发送提醒；
    如果单价发生改变，则会自动修改cost并且向收件箱发送提醒"""
    if request.method == "GET":
        form = order_form()
        return render(request, "_form.html", {"form": form, "form_name": "添加进货记录", "people_name": request.session.get('name')})
    
    form = order_form(data=request.POST)
    
    if form.is_valid():
        supplier_name = request.POST.get("supplier_name").strip()
        shop_name = request.POST.get("shop_name").strip()
        goods_name = request.POST.get("goods_name").strip()
        goods_order_num = request.POST.get("goods_order_num")
        cost_money = request.POST.get("cost_money")
        
        ## 增加remian中的库存量，若不存在则创建，若存在则在原有数量上增加
        remain = models.remain.objects.filter(shop_name=shop_name, goods_name=goods_name).values_list("goods_remain", flat=True)
        if not remain:
            models.remain.objects.create(shop_name=shop_name, goods_name=goods_name, goods_remain=int(goods_order_num))
        else:
            models.remain.objects.filter(shop_name=shop_name, goods_name=goods_name).update(goods_remain = int(remain[0]) + int(goods_order_num))

        ## 获取obj对象和当前进货单价
        goods_obj = models.goods.objects.filter(name=goods_name)
        cost_obj = models.cost.objects.filter(supplier_name=supplier_name, goods_name=goods_name)
        current_cost_unit = eval(cost_money + '/' + goods_order_num)
        ## 商品和对应的供应商均存在
        if goods_obj and cost_obj:
            cost_instance = cost_obj.first() 
            previous_cost_unit = cost_instance.cost_unit
            if current_cost_unit != previous_cost_unit:
                compare = 1 if current_cost_unit < previous_cost_unit else 3 # 与上一次进货单价比较，为1则小于，3则大于
                goods_obj.update(status="未确认")
                cost_obj.update(cost_unit=current_cost_unit, status="已进货", compare=compare)
                send_info_to_mail(cost_instance.supplier_name, cost_instance.goods_name, previous_cost_unit, current_cost_unit)
        ## goods_obj 或者 cost_obj 其中一个 不存在，则创建
        else:
            compare = 2
            sell_unit = round(COST_TO_GOODS * current_cost_unit, 2)
            if not goods_obj:
                mail_text = "新建了<b>" + supplier_name + "</b>供应的<b>" + goods_name + "</b>单价信息，进货单价为" + str(round(current_cost_unit, 2)) + "元，请及时到商品单价界面查看！"
                if cost_obj:
                    compare = 1 if current_cost_unit < cost_obj.first().cost_unit else 3
                models.mail.objects.create(type=2, text=mail_text)
                models.goods.objects.create(type=1, name=goods_name, unit_sale=sell_unit, measurement="个")
                if cost_obj:
                    models.cost.objects.filter(supplier_name=supplier_name, goods_name=goods_name).update(cost_unit=current_cost_unit, status="已进货", compare=compare) 
                else:
                    models.cost.objects.create(supplier_name=supplier_name, goods_name=goods_name, cost_unit=current_cost_unit, status="已进货", compare=compare) 
            
            ## goods存在，cost不存在
            else:
                models.cost.objects.create(supplier_name=supplier_name, goods_name=goods_name, cost_unit=current_cost_unit, status="已进货")
                goods_obj.update(status="未确认")
                mail_text = "新建了<b>" + supplier_name + "</b>供应的<b>" + goods_name + "</b>单价信息，进货单价为" + str(round(current_cost_unit, 2)) + "元，请及时到商品单价界面查看！"
                models.mail.objects.create(type=2, text=mail_text)            
        ## form 进货记录保存
        form.save()
        return redirect("/order/list")
    return render(request, '_form.html', {"form": form, "form_name": "添加进货记录", "people_name": request.session.get('name')})

@session_check("per")
def order_download(request, type: int):
    '''
    导出信息进货记录
    '''
    global DOWNLOAD_PATH
    file_path = DOWNLOAD_PATH[type]
    # 将订单记录写入文件中，利用pandas库
    if type == 2:
        database_dump(models.order_record, DOWNLOAD_PATH[2],["订单号", "供应商", "商品名", "订货数量", "支付金额", "接收商品的门店", "日期"])

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response

@session_check("per")
def order_upload(request):
    '''
    读取上传的文件，将信息写入数据库中，并返回错误信息
    '''
    if request.method == "POST":
        form = file_form(request.POST, request.FILES)
        uploaded_file = request.FILES['file']
        # check if the uploaded file is legal
        allowed_formats = ['.csv', '.xlsx', '.xls']
        file_pure_name, file_ext = os.path.splitext(uploaded_file.name)[0], os.path.splitext(uploaded_file.name)[1].lower()
        max_size = 20 * 1024 * 1024
        
        # check the format and size of the file
        if not file_ext in allowed_formats:
            return render(request, '_upload.html', {"form": form, "people_name": request.session.get('name'), "process_result": "无效的文件格式，请重新上传！"})
        if uploaded_file.size > max_size:
            return render(request, '_upload.html', {"form": form, "people_name": request.session.get('name'), "process_result": "文件大小超过20MB！"})
        # change the file name to the current timestamp
        timestamp = str(time.time()).split('.')[0]
        file_absolute_path = 'backup/' + timestamp + file_ext 
        # save the file in ./backup/
        with open(file_absolute_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        clear_upload_files()
        # read the file by pandas
        total_len = 0
        error_msg, total_len = read_datafile(file_absolute_path)
        if error_msg != "":
            return render(request, '_upload.html', {"form": form, "people_name": request.session.get('name'), "process_result": error_msg})
        # if total_len != -1, all data in the uploaded file is written into the database
        if total_len != -1:
            return render(request, '_upload.html', {"form": form, "people_name": request.session.get('name'),  
                                                    "process_result": "<p style='color: green; display: inline'>文件已成功上传，共写入%d条订单记录！</p>"%total_len})
        return render(request, '_upload.html', {"form": form, "people_name": request.session.get('name')})
    else:
        form = file_form()
    return render(request, '_upload.html', {"form": form, "people_name": request.session.get('name')})


######################################################################
#                               sale                                 #
######################################################################

@session_check("per")
def sale_list(request):
    """展示所有门店的销售记录"""
    data_list = models.sale_record.objects.filter()
    total_len = len(data_list)
    table_header = ["编号", "商店名称", "商品名", "售出量","毛利", "销售时间"] 
    table_body = [
        [total_len - obj.id + 1 for obj in data_list],
        [obj.shop_name for obj in data_list],
        [obj.goods_name for obj in data_list],
        [obj.goods_sale_num for obj in data_list],
        [float_right_align(obj.turnover) for obj in data_list],
        [obj.sale_time.strftime('%Y-%m-%d %H:%M:%S') for obj in data_list],
    ]
    table_body = transpose_list(table_body)
    return render(request, "_list.html", {"table_header": table_header, "table_body": table_body, "list_name": "销售记录表", "people_name": request.session.get("name")})


######################################################################
#                              remain                                #
######################################################################

# 仅支持查看的库存信息表
@session_check("per")
def remain_list(request):
    """展示所有商店的所有商品的库存信息"""
    data_list = models.remain.objects.filter()
    table_header = ["编号", "商店", "商品名", "余量"] 
    table_body = [
        [obj.id for obj in data_list],
        [obj.shop_name for obj in data_list],
        [obj.goods_name for obj in data_list],
        [obj.goods_remain for obj in data_list],
    ]
    table_body = transpose_list(table_body)
    return render(request, "_list.html", {"table_header": table_header, "table_body":table_body, "list_name": "库存记录表", "people_name": request.session.get('name')})


######################################################################
#                               mail                                 #
######################################################################

# 收件箱，可以搜索，可以按照不同类型进行选取
@session_check("per")
def mail_list(request, nid):
    """展示收件箱中的内容"""
    if nid == 0:
        data_list = models.mail.objects.filter()
        total_len = len(data_list)
        table_header = ["编号", "时间", "提醒内容", "类别"] 
        table_body = [
            [total_len - _ for _ in range(total_len)],
            [time_formatter(obj.time) for obj in data_list],
            [obj.text for obj in data_list],
            [MAIL_TYPE[obj.type - 1] for obj in data_list],
        ]
    else:
        data_list = models.mail.objects.filter(type=nid)
        total_len = len(data_list)
        table_header = ["编号", "时间", "提醒内容"] 
        table_body = [
            [total_len - i for i in range(total_len)],
            [time_formatter(obj.time) for obj in data_list],
            [obj.text for obj in data_list],
        ]
    table_body = transpose_list(table_body)
    return render(request, "_list.html", {"table_header": table_header, "table_body": table_body, "list_name": "收件箱", "people_name": request.session.get('name')})
