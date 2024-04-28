from rest_framework.decorators import api_view
from e_commerce_apis.source.modules.RegisterUser import RegisterUser
from e_commerce_apis.source.modules.LoginUser import LoginUser
from e_commerce_apis.source.modules.GetUserDetails import GetUserDetails
from e_commerce_apis.source.modules.GetProductDetails import GetProductDetails
from  e_commerce_apis.source.modules.UserCartManagement import UserCartManagement
from  e_commerce_apis.source.modules.GetUserCartDetails import GetUserCartDetails
from  e_commerce_apis.source.modules.CreateNewUserAddress import CreateNewUserAddress
from  e_commerce_apis.source.modules.UserOrderConfirmation import UserOrderConfirmation
from  e_commerce_apis.source.modules.GetCurrencyDetails import GetCurrencyDetails
from  e_commerce_apis.source.modules.FetchProductDetails import FetchProductDetails
from  e_commerce_apis.source.modules.GetUserAddressDetails import GetUserAddressDetails
from  e_commerce_apis.source.modules.GetUserOrderDetails import GetUserOrderDetails
from  e_commerce_apis.source.modules.GetUserPictureDetails import GetUserpictureDetails
from e_commerce_apis.source.modules.GetCountryDetails  import GetCountryDetails
from e_commerce_apis.source.modules.GetStateDetails  import GetStateDetails
from e_commerce_apis.source.modules.GetAreaDetails  import GetAreaDetails
from e_commerce_apis.source.modules.DeleteUserCartDetails import DeleteUserCartDetails

# Create your views here.
@api_view(['post'])
def register_user_view(request):
    return RegisterUser.register_user(request)

@api_view(['post'])
def login_user_view(request):
    return LoginUser.login_user(request)

@api_view(['post'])
def get_country_view(request):
    return GetCountryDetails.get_country_details(request)

@api_view(['post'])
def delete_user_cart_view(request):
    return DeleteUserCartDetails.delete_user_cart_details(request)

@api_view(['post'])
def get_state_view(request):
    return GetStateDetails.get_state_details(request)

@api_view(['post'])
def get_area_view(request):
    return GetAreaDetails.get_area_details(request)

@api_view(['post'])
def newaddress_user_view(request):
    return CreateNewUserAddress.create_new_user_address(request)

@api_view(['get'])
def fetchproduct_user_view(request):
    return FetchProductDetails.fetch_product_details(request)

@api_view(['post'])
def getcurrency_user_view(request):
    return GetCurrencyDetails.get_currency_details(request)

@api_view(['post'])
def getproduct_user_view(request):
    return GetProductDetails.get_product_details(request)

@api_view(['post'])
def getuseradd_user_view(request):
    return GetUserAddressDetails.get_user_address_details(request)

@api_view(['post'])
def getusercart_user_view(request):
    return GetUserCartDetails.get_user_cart_details(request)

@api_view(['post'])
def getuser_user_view(request):
    return GetUserDetails.get_user_details(request)

@api_view(['post'])
def getuserorder_user_view(request):
    return GetUserOrderDetails.get_user_order_details(request)

@api_view(['post'])
def getuserpic_user_view(request):
    return GetUserpictureDetails.get_user_picture_details(request)

@api_view(['post'])
def cartmanagement_user_view(request):
    return UserCartManagement.user_cart_management(request)

@api_view(['post'])
def orderconfirmation_user_view(request):
    return UserOrderConfirmation.user_order_confirmation(request)


