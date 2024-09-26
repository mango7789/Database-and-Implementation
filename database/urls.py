"""
URL configuration for database project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from manager import views as mg_views
from staff import views as st_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler403, handler500
from .handler import *

# error handler
handler403 = error_403_view
handler404 = error_404_view
handler500 = error_500_view

# basic urls
urlpatterns = [

    ######################################################################
    #                           admin module                             #
    ######################################################################

    path('logout/', mg_views.log_out, name='logout'),

    # 管理员信息/admin
    path('admin', mg_views.admin),

    # 登录界面，在管理层模块中定义/log in
    path('',mg_views.log_in),

    # 主页/homepage
    path('homepage',mg_views.homepage),

    # 帮助文档/help
    path('help', mg_views.help),

    # 门店，员工/shop, salesman
    path('shop/list/', mg_views.shop_list),
    path('shop/add/', mg_views.shop_add),
    path('shop/<int:nid>/modify/', mg_views.shop_modify),
    path('shop/<int:nid>/salesman/', mg_views.shop_salesman),
    path('shop/<int:nid>/salesman/add/', mg_views.shop_salesman_add),
    path('shop/<int:nid>/salesman/modify/', mg_views.shop_salesman_modify),
    path('shop/<int:nid>/salesman/delete/', mg_views.shop_salesman_delete),

    # 供应商/supplier
    path('supplier/list/', mg_views.supplier_list),
    path('supplier/add/', mg_views.supplier_add),
    path('supplier/<int:nid>/modify/', mg_views.supplier_modify),

    # 商品/goods
    path('goods/list/', mg_views.goods_list),
    path('goods/<int:nid>/modify/', mg_views.goods_modify),

    # 进价单价信息/cost
    path('cost/list/', mg_views.cost_list),
    path('cost/add/', mg_views.cost_add),
    path('cost/<int:nid>/modify/', mg_views.cost_modify),

    # 进货模块/order
    path('order/list/', mg_views.order_list),
    path('order/add/', mg_views.order_add),
    path('order/download/<int:type>/', mg_views.order_download),
    path('order/upload/', mg_views.order_upload),

    # 销售记录信息/sale
    path('sale/list/', mg_views.sale_list),

    # 库存/remain
    path('remain/list/', mg_views.remain_list), 

    # 收件箱/mail
    path('mail/<int:nid>/list/', mg_views.mail_list),


    ######################################################################
    #                           staff module                             #
    ######################################################################

    # 门店信息/staff~shop
    path('staff/shop/list/', st_views.staff_shop_list),  

    # 库存/staff~goods
    path('staff/goods/list/', st_views.staff_goods_list), 

    # 销售/staff~sale~add
    path('staff/sale/<int:nid>/add/', st_views.staff_sale_receipt_add),  # 此处的nid是商品在goods表中的id

    # 销售历史记录/staff~sale~list
    path('staff/sale/list/', st_views.staff_sale_list), 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
