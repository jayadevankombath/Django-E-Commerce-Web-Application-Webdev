"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url,include
from .import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'adminlogout/$',views.adminlogout,name="adminlogout"),
    url(r'admin_logpage/$',views.admin_logpage,name="adminlogpage"),
    url(r'logadmin/$',views.logadmin,name="logadmin"),
    url(r'addproduct/$',views.addproduct,name="addproduct"),
    url(r'adminhome/$',views.adminhome,name="adminhome"),
    url(r'upload_product/$',views.upload_product,name="upload_product"),
    url(r'delete_pro/(?P<id>\d+)$',views.delete_pro,name="delete_pro"),
    url(r'edit_pro/(?P<id>\d+)$',views.edit_pro,name="edit_pro"),
    url(r'upload_pro/(?P<id>\d+)$',views.upload_pro,name="upload_pro"),
    url(r'purchase/$',views.purchase,name="purchase"),
    url(r'uploadpur/$',views.uploadpur,name="uploadpurchase"),
    url(r'viewpur/$',views.viewpur,name="viewpur"),
    url(r'del_purchase/(?P<id>\d+)$',views.del_purchase,name="del_purchase"),
    url(r'view_stockes/$',views.view_stockes,name="view_stockes"),
    url(r'editstock/(?P<id>\d+)$',views.editstock,name="editstock"),
    url(r'update_stock/(?P<id>\d+)$',views.update_stock,name="update_stock"),
    url(r'userlist/$',views.userlist,name="userlist"),
    url(r'removeUser/(?P<id>\d+)$',views.removeUser,name="removeUser"),
    url(r'view_sales/$',views.view_sales,name="view_sale"),
    url(r'del_sale/(?P<id>\d+)$',views.del_sale,name="delete_sale"),
    url(r'product_data/(?P<id>\d+)$',views.product_data,name="product_data"),
    url(r'buy/(?P<id>\d+)$',views.buy,name="buy_product"),
    url(r'user_home/$',views.user_home,name="user_home"),
    url(r'login_page/$',views.login_page,name="login_page"),
    url(r'reg/$',views.reg,name="new_user"),
    url(r'reg_user/$',views.reg_user,name="reg_user"),
    url(r'usr/$',views.usr,name="userlog"),
    url(r'ulogout/$',views.ulogout,name="userlogout"),
    url(r'search/$',views.search,name="searching"),

]
