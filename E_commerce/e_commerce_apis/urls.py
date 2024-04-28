from django.urls import re_path
from .views import (register_user_view,
                    login_user_view,
                    newaddress_user_view,delete_user_cart_view,
                    fetchproduct_user_view,getcurrency_user_view,getproduct_user_view,
                    getuseradd_user_view,getusercart_user_view,getuser_user_view,
                    getuserorder_user_view, get_country_view, get_area_view, get_state_view,
                    getuserpic_user_view,cartmanagement_user_view,orderconfirmation_user_view)

urlpatterns=[
    re_path(r"^ecommerceapi/register-user/?$",register_user_view,name="register_user"),
    re_path(r"^ecommerceapi/login-user/?$",login_user_view,name="login_user"),
    re_path(r"^ecommerceapi/get-country/?$",get_country_view,name="get_country"),
    re_path(r"^ecommerceapi/get-state/?$",get_state_view,name="get_state"),
    re_path(r"^ecommerceapi/get-area/?$",get_area_view,name="get_area"),
    re_path(r"^ecommerceapi/delete-user-cart/?$",delete_user_cart_view,name="delete_user_cart"),
    re_path(r"^ecommerceapi/newaddress-user/?$",newaddress_user_view,name="newaddress_user"),
    re_path(r"^ecommerceapi/getcurrency-user/?$",getcurrency_user_view,name="getcurrency_user"),
    re_path(r"^ecommerceapi/fetchproduct-user/?$",fetchproduct_user_view,name="fetchproduct_user"),
    re_path(r"^ecommerceapi/getproduct-user/?$",getproduct_user_view,name="getproduct_user"),
    re_path(r"^ecommerceapi/getuseradd-user/?$",getuseradd_user_view,name="getuseradd_user"),
    re_path(r"^ecommerceapi/getusercart-user/?$",getusercart_user_view,name="getusercart_user"),
    re_path(r"^ecommerceapi/getuser-user/?$",getuser_user_view,name="getuser_user"),
    re_path(r"^ecommerceapi/getuserorder-user/?$",getuserorder_user_view,name="getuserorder_user"),
    re_path(r"^ecommerceapi/getuserpic-user/?$",getuserpic_user_view,name="getuserpic_user"),
    re_path(r"^ecommerceapi/cartmanagement-user/?$",cartmanagement_user_view,name="cartmanagement_user"),
    re_path(r"^ecommerceapi/orderconfirmation-user/?$",orderconfirmation_user_view,name="orderconfirmation_user")
]