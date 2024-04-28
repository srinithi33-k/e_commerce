# from e_commerce_apis.source.common.query_constants import USER_PROFILE
from e_commerce_apis.source.common.common_utils import cursor_creater
from e_commerce_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from e_commerce_apis.source.common.query_constants import   COUNTRY,AREA,STATE,USER_PROFILE,USER_ADDRESS_MANAGEMENT,PRODUCT_TYPE_CATEGORY,SUB_CATEGORY_PRODUCT,PRICE_DECISION_FECTOR,CURRENCY,SELLER_CATEGORY,PRODUCT_PICTURE_CATEGORY,PRODUCT_TABLE,VARIENT_CATEGORY,USER_ORDER_MANAGEMENT,USER_CART_MANAGEMENT,VARIENT_CATEGORY
connect,cursor =cursor_creater()
# co/nnect,cursor =cursor_creater()
# cursor.execute(COUNTRY)
# connect.commit()
# cursor.execute(STATE)
# connect.commit()
# cursor.execute(AREA)
# connect.commit()
# cursor.execute(CURRENCY)
# connect.commit()
# cursor.execute(USER_PROFILE)
# connect.commit()
# cursor.execute(USER_ADDRESS_MANAGEMENT)
# connect.commit()
# cursor.execute(PRODUCT_TYPE_CATEGORY)
# connect.commit()
# cursor.execute(SUB_CATEGORY_PRODUCT)
# connect.commit()
# cursor.execute(PRICE_DECISION_FECTOR)
# connect.commit()
# cursor.execute(SELLER_CATEGORY)
# connect.commit()
cursor.execute(PRODUCT_PICTURE_CATEGORY)
connect.commit()
# cursor.execute(VARIENT_CATEGORY)
# connect.commit()
# cursor.execute(PRODUCT_TABLE)
# connect.commit()

# cursor.execute(USER_ORDER_MANAGEMENT)
# connect.commit()
# cursor.execute(USER_CART_MANAGEMENT)
# connect.commit()

# if cursor.statusmessage== "CREATE TABLE":
print(GOOD_JSON) 
# else:
#     print(ERROR_JSON)    