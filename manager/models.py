from django.db import models

# Create your models here.
class supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True, verbose_name="该名称")
    telephone = models.CharField(max_length=11, unique=True, verbose_name="该电话")
    email = models.CharField(max_length=30, null=True, unique=True, verbose_name="该邮箱")
    class Meta:
        verbose_name = "供应商"

class manager(models.Model):
    # avatar = models.ImageField(upload_to='/src/img', default='/src/img/user.png')
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=10)


class shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True, verbose_name="该名称")  # 门店名称，唯一
    location = models.CharField(max_length=15)  # 门店位置
    location_specific = models.CharField(max_length=20, default="")
    telephone = models.CharField(max_length=11, unique=True, verbose_name="该电话号码")  # 第一个电话，唯一
    salesman_name = models.CharField(max_length=10)
    status_choices = (
        (1, '营业'),
        (2, '停业'),
    )
    status = models.SmallIntegerField(verbose_name="营业状态", choices=status_choices, default=1)
    class Meta:
        verbose_name = "商店"



class goods(models.Model):  # 商品信息表，注意，包含销售单价信息
    id = models.AutoField(primary_key=True)
    type_choice = (
        (1, '食品'),
        (2, '日用百货'),
        (3, '服装鞋帽'),
        (4, '数码产品'),
        (5, '文体用品')
    )
    type = models.SmallIntegerField(verbose_name="商品类别", choices=type_choice, default=1)  # 商品类别，枚举
    name = models.CharField(max_length=20)  # 商品名称
    unit_sale = models.DecimalField(max_digits=8, decimal_places=2)  # 商品销售单价
    measurement = models.CharField(max_length=5)  # 商品计量单位
    status = models.CharField(default="未确认", max_length=3)


class cost(models.Model):  # 进货单价表
    id = models.AutoField(primary_key=True)  # 自动生成主键
    supplier_name = models.CharField(default=None, max_length=20)  # 外键约束放到钩子函数进行处理
    goods_name = models.CharField(default=None, max_length=20, db_index=True)   # 外键约束放到钩子函数进行处理
    cost_unit = models.DecimalField(max_digits=8, decimal_places=2)  # 进货单价
    status = models.CharField(default="预订购", max_length=3)
    compare = models.SmallIntegerField(default=2)
    class Meta:  # 联合唯一性，防止输入同一个供应商+同一个商品的情况
        unique_together = ('supplier_name', 'goods_name')


class order_record(models.Model):  # 进货记录表
    id = models.AutoField(primary_key=True)  # 自动生成主键
    supplier_name = models.CharField(default=None, max_length=20)  # 外键约束放到钩子函数进行处理
    goods_name = models.CharField(default=None, max_length=20, db_index=True)   # 外键约束放到钩子函数进行处理
    goods_order_num = models.SmallIntegerField()  # 进货的商品数量
    cost_money = models.DecimalField(max_digits=12, decimal_places=2)  # 向供应商支付的金额
    shop_name = models.CharField(default=None, max_length=20)   # 外键约束放到钩子函数进行处理
    order_time = models.DateTimeField(auto_now_add=True)  # 本次进货的日期，自动添加


class sale_record(models.Model):  # 销售记录表 - 子开在写
    id = models.AutoField(primary_key=True)  # 自动生成主键
    shop_name = models.CharField(default=None, max_length=20)   # 外键约束放到钩子函数进行处理
    goods_name = models.CharField(default=None, max_length=20, db_index=True)   # 外键约束放到钩子函数进行处理
    goods_sale_num = models.SmallIntegerField()
    turnover = models.DecimalField(max_digits=10, decimal_places=2)  # 本次销售的毛利
    sale_time = models.DateTimeField(auto_now_add=True)  # 本次销售的日期，自动添加
    sale_man_id = models.IntegerField()


class remain(models.Model):  # 库存记录表
    id = models.AutoField(primary_key=True)  # 自动生成主键
    shop_name = models.CharField(default=None, max_length=20)   # 外键约束放到钩子函数进行处理
    goods_name = models.CharField(default=None, max_length=20, db_index=True)   # 外键约束放到钩子函数进行处理
    goods_remain = models.SmallIntegerField()


class mail(models.Model):    
    id = models.AutoField(primary_key=True)
    text = models.CharField(default=None, max_length=80)
    time = models.DateTimeField(auto_now_add=True)
    type = models.SmallIntegerField()
