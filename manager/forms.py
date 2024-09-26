from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from manager import models as mg_models
from staff import models as st_models
from .utils import is_valid_string, load_json

######################################################################
#                             log in                                 #
######################################################################

class loginform(forms.Form):
    type = forms.IntegerField(label="身份")
    id = forms.IntegerField(label="ID", widget=forms.NumberInput, required=True)
    password = forms.CharField(label="密码", widget=forms.PasswordInput, required=True)

######################################################################
#                              shop                                  #
######################################################################

province_city = load_json('./static/files/save.json')
provinces, cities = [("---", "---")], [("---", "---")]
for province in list(province_city.keys()):
    provinces.append((province, province))
for city in province_city.values():
    for _ in city:
        cities.append((_, _))

class shopform(forms.ModelForm):
    name = forms.CharField(max_length=20, label="商店名称")
    province = forms.ChoiceField(choices=provinces, label="省份、直辖市或自治区")
    city = forms.ChoiceField(choices=cities, label="市或区")
    location = forms.CharField(max_length=20, label="详细地址")
    telephone = forms.CharField(label="电话号码", validators=[RegexValidator(r'^1[3-9]\d{9}$', '电话号码格式错误')])
    salesman_name = forms.CharField(max_length=10, label='负责人')
    # status = forms.IntegerField(label='营业状态')

    class Meta:
        model = mg_models.shop
        fields = ['name', 'province', 'city', 'location', 'telephone', 'salesman_name']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


class shopform_modify(forms.ModelForm):
    id = forms.IntegerField(disabled=True, label="编号")
    name = forms.CharField(max_length=20, label="商店名称")
    previous = forms.CharField(disabled=True, required=False, label="原地址")
    location_specific = forms.CharField(max_length=20, label="详细地址")
    telephone = forms.CharField(label="电话号码",
                                  validators=[RegexValidator(r'^1[3-9]\d{9}$', '电话号码格式错误')])
    salesman_name = forms.CharField(max_length=10, label='负责人')
    # status = forms.IntegerField(label='营业状态')

    class Meta:
        model = mg_models.shop
        fields = ['id', 'name', 'location_specific', 'telephone', 'salesman_name']
    field_order = ['id', 'previous', 'name', 'location_specific', 'telephone', 'salesman_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


######################################################################
#                            salesman                                #
######################################################################

class salesmanform(forms.ModelForm):
    shop_name = forms.CharField(max_length=20, label="所属商店") 
    salesman_name = forms.CharField(max_length=10, label="员工姓名")
    salesman_password = forms.CharField(max_length=20, label="员工密码")

    class Meta:
        model = st_models.salesman
        fields = ['shop_name', 'salesman_name', 'salesman_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}
        self.fields['salesman_password'].validators.append(self.validate_password)

    def validate_password(self, password):
        # 密码长度至少为8
        if len(password) < 8:
            raise ValidationError(
                "密码长度至少为8"
            )
        required_classes = {
            'uppercase': any(c.isupper() for c in password),
            'lowercase': any(c.islower() for c in password),
            'numeric': any(c.isdigit() for c in password),
            'special_characters': any(c for c in password if c.isalnum() is False),
        }
        # 至少包含三种符号
        if sum(map(int, required_classes.values())) < 3:
            raise ValidationError(
                "密码必须包含大写字母、小写字母、数字或特殊符号(如：-*)中的至少三种"
            )
        
    def clean_shop_name(self):
        input_shop_name = self.cleaned_data['shop_name']
        goods_name_set = list(mg_models.shop.objects.values_list('name', flat=True))
        if input_shop_name not in goods_name_set:
            raise ValidationError('不存在该商店')
        return input_shop_name

class salesmanmodifyform(forms.ModelForm):
    id = forms.IntegerField(label="员工编号", disabled=True)
    salesman_name = forms.CharField(max_length=10, label="员工姓名", disabled=True)
    salesman_password = forms.CharField(max_length=20, label="员工密码")
    shop_name = forms.CharField(disabled=True, label="商店名称", required=False)

    class Meta:
        model = st_models.salesman
        fields = ['id', 'shop_name', 'salesman_name', 'salesman_password']

    field_order = ['id', 'shop_name', 'salesman_name', 'salesman_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}
        self.fields['salesman_password'].validators.append(self.validate_password)
    
    def validate_password(self, password):
        # 密码长度至少为8
        if len(password) < 8:
            raise ValidationError(
                "密码长度至少为8"
            )
        required_classes = {
            'uppercase': any(c.isupper() for c in password),
            'lowercase': any(c.islower() for c in password),
            'numeric': any(c.isdigit() for c in password),
            'special_characters': any(c for c in password if c.isalnum() is False),
        }
        # 至少包含三种符号
        if sum(map(int, required_classes.values())) < 3:
            raise ValidationError(
                "密码必须包含大写字母、小写字母、数字或特殊符号(如：-*)中的三种"
            )
        

######################################################################
#                            supplier                                #
######################################################################

class supplierform(forms.ModelForm):
    name = forms.CharField(max_length=20, label="供应商名称")
    telephone = forms.CharField(label="电话号码", validators=[RegexValidator(r'^1[3-9]\d{9}$', '电话号码格式错误')])
    email = forms.CharField(label="邮箱", validators=[
                RegexValidator(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$', "邮箱格式错误")
            ])

    class Meta:
        model = mg_models.supplier
        fields = ['name', 'telephone', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

class supplierform_modify(forms.ModelForm):
    id = forms.IntegerField(disabled=True, label="编号")
    name = forms.CharField(max_length=20, label="供应商名称")
    telephone = forms.CharField(label="电话号码", validators=[RegexValidator(r'^1[3-9]\d{9}$', '电话号码格式错误')])
    email = forms.CharField(label="邮箱", validators=[
        RegexValidator(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$',
                       "邮箱格式错误")])

    class Meta:
        model = mg_models.supplier
        fields = ['id', 'name', 'telephone', 'email']

    field_order = ['id', 'name', 'telephone', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


######################################################################
#                             goods                                  #
######################################################################

class goodsform_modify(forms.ModelForm):
    order_unit = forms.DecimalField(max_digits=8, decimal_places=2, label="进货平均单价", disabled=True, required=False)
    type = forms.IntegerField(disabled=False, label="类别") 
    name = forms.CharField(max_length=20, label='商品名称', disabled=True)  # 商品名称
    unit_sale = forms.DecimalField(max_digits=8, decimal_places=2, label='销售单价')  # 商品销售单价
    measurement = forms.CharField(max_length=5, label='计量单位')  # 商品计量单位

    class Meta:
        model = mg_models.goods
        fields = ['type', 'name', 'unit_sale', 'measurement', "order_unit"]

    field_order = ['name', 'type', 'order_unit', 'unit_sale', 'measurement']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].widget = forms.Select(choices=mg_models.goods.type_choice) # 添加select的表单形式即可展示choices的文本信息
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


######################################################################
#                              cost                                  #
######################################################################
            
class cost_form(forms.ModelForm):
    # 这里似乎无法对supplier_id和goods_id进行外键约束检查 -- 使用钩子方法 
    supplier_name = forms.CharField(label="供应商名称")
    goods_name = forms.CharField(label="商品名称")
    cost_unit = forms.DecimalField(max_digits=8, decimal_places=2, label="进货单价")

    class Meta:
        model = mg_models.cost
        fields = ['supplier_name', 'goods_name', 'cost_unit']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    # 使用钩子方法进行外键约束的检查
    def clean_supplier_name(self):
        input_supplier_name = self.cleaned_data['supplier_name']
        # 先把所有的供应商名称提取出来
        supplier_name_set = list(mg_models.supplier.objects.values_list('name', flat=True))
        if input_supplier_name not in supplier_name_set:
            raise ValidationError('该供应商不存在，请先创建')
        # 如果存在则返回用户输入的值
        return input_supplier_name

    def clean_goods_name(self):
        input_goods_name = self.cleaned_data['goods_name']
        input_supplier_name = self.data.get('supplier_name')
        goods_and_supplier = list(mg_models.cost.objects.values_list('goods_name', 'supplier_name'))
        if (input_goods_name,input_supplier_name) in goods_and_supplier:
            raise ValidationError('已经储存过这个供应商提供该商品的进货单价信息')
        return input_goods_name
    
class costform_modify(forms.ModelForm):
    supplier_name = forms.CharField(label="供应商名称", disabled=True)
    goods_name = forms.CharField(label="商品名称", disabled=True)
    cost_unit = forms.DecimalField(max_digits=8, decimal_places=2, label="进货单价")

    class Meta:
        model = mg_models.cost
        fields = ['id', 'supplier_name', 'goods_name', 'cost_unit']

    fields_order = ['id', 'supplier_name', 'goods_name', 'cost_unit']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

######################################################################
#                              order                                 #
######################################################################
            
class order_form(forms.ModelForm):
    supplier_name = forms.CharField(label="供应商名称")
    goods_name = forms.CharField(label="商品名称")
    goods_order_num = forms.IntegerField(label='进货数量')
    cost_money = forms.DecimalField(max_digits=12, decimal_places=2, label='向供应商支付金额')
    shop_name = forms.CharField(max_length=20, label='商店名称')

    class Meta:
        model = mg_models.order_record
        fields = ['supplier_name', 'shop_name', 'goods_name', 'goods_order_num', 'cost_money']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    # 使用钩子方法进行外键约束的检查
    def clean_supplier_name(self):
        input_supplier_name = self.cleaned_data['supplier_name']
        # 先把所有的供应商名称提取出来
        supplier_name_set = list(mg_models.supplier.objects.values_list('name', flat=True))
        if input_supplier_name not in supplier_name_set:
            raise ValidationError('该供应商不存在，请先创建')
        # 如果存在则返回用户输入的值
        return input_supplier_name

    def clean_shop_name(self):
        input_shop_name = self.cleaned_data['shop_name']
        # 先把所有的门店提取出来
        shop_name_set = list(mg_models.shop.objects.values_list('name', flat=True))
        if input_shop_name not in shop_name_set:
            raise ValidationError('该门店不存在，请先创建')
        # 如果存在则返回用户输入的值
        return input_shop_name
    
    def clean_goods_name(self):
        input_goods_name = self.cleaned_data['goods_name']
        if not is_valid_string(input_goods_name):
            raise ValidationError("该商品名称不规范，请重新输入！")
        return input_goods_name
    
class file_form(forms.Form):
    file = forms.FileField(label="支持.csv,.xls和.xlsx格式，文件大小不超过20MB", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}
