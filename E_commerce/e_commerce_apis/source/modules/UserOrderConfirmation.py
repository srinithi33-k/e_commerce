from e_commerce_apis.source.common.query_constants import FETCH_AVAILABILITY_COUNT,UPDATE_PRODUCT_COUNT,insert_query_marker
from e_commerce_apis.source.common.common_utils import cursor_creater,token_validator
from datetime import datetime
from e_commerce_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from django.http import JsonResponse
from json import loads

class UserOrderConfirmation:
    @staticmethod
    def user_order_confirmation(request):
        try:
            
            sample_dict=loads(request.body)
            if not token_validator(request.headers.get("Authorization"),sample_dict.get("user_id")):
                raise Exception("invalid user!")
            # sample_dict={"user_id":5001,"product_id":13008,"address_id":6000}
            field=sample_dict.get("product_id"),
            select_query=FETCH_AVAILABILITY_COUNT%field
            connect,cursor= cursor_creater()
            cursor.execute(select_query)
            existing_count=cursor.fetchall()[0]
            # print(existing_count)
            if len(existing_count) == 1 and existing_count.get("availability_count")>=1:
                # print(existing_count)
                new_count=existing_count.get("availability_count")-1
                update_field_1=new_count,sample_dict.get("product_id")
                update_field=UPDATE_PRODUCT_COUNT%update_field_1
                cursor.execute(update_field)
                connect.commit()
                
                sample_dict["user_id"]=str(sample_dict.get("user_id"))
                sample_dict["product_id"]=str(sample_dict.get("product_id"))
                sample_dict["address_id"]=str(sample_dict.get("address_id"))
                sample_dict={"user_id":sample_dict["user_id"],"product_id":sample_dict["product_id"],"ordered_on":datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"address_id":sample_dict["address_id"],"ordered_status":"packing"}
                sample_dict={key:"'"+ value +"'" for key,value in sample_dict.items()}  
                insert_query=insert_query_marker("user_order_management",sample_dict)
                # print(insert_query)
                cursor.execute(insert_query)
                connect.commit()
                # print(GOOD_JSON)
                return JsonResponse(GOOD_JSON,status=200)
                
            else:
                raise Exception("out of stock!")    

        except Exception as error:
            ERROR_JSON["reason"]=str(error)
            return JsonResponse(ERROR_JSON,status=400)










