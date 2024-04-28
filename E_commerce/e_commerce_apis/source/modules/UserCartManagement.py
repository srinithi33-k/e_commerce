from e_commerce_apis.source.common.query_constants import FETCH_CART ,UPDATE_CART ,insert_query_marker
from e_commerce_apis.source.common.common_utils import cursor_creater,token_validator
from e_commerce_apis.source.common.constants import GOOD_JSON,ERROR_JSON 
from django.http import JsonResponse
from json import loads

class UserCartManagement:
    @staticmethod
    def user_cart_management(request):
        try:
            # sample_dict={"user_id":5001,"product_id":13008,"quantity":1}
            sample_dict=loads(request.body)
            if not token_validator(request.headers.get("Authorization"),sample_dict.get("user_id")):
                raise Exception("invalid user!")
                           
            sample_dict["user_id"]=str(sample_dict.get("user_id"))
            sample_dict["product_id"]=str(sample_dict.get("product_id"))
            sample_dict["quantity"]=str(sample_dict.get("quantity"))

            field=(sample_dict["user_id"],sample_dict["product_id"])
            recode=FETCH_CART%field
            connect,cursor=cursor_creater()
            cursor.execute(recode)
            existing_record=cursor.fetchall()
            if len(existing_record) == 1:
                
                new_quantity=existing_record[0].get("quantity")+int(sample_dict["quantity"])
                field_2=new_quantity,sample_dict["user_id"],sample_dict["product_id"]
                update_query=UPDATE_CART%field_2
                cursor.execute(update_query)
                connect.commit()
                # print(GOOD_JSON)
                return JsonResponse(GOOD_JSON,status=200)
            else:
                sample_dict={key:"'"+ value +"'" for key,value in sample_dict.items()}
                insert_query=insert_query_marker("user_cart_management",sample_dict)
                cursor.execute(insert_query)
                connect.commit()
                # print(GOOD_JSON)
                return JsonResponse(GOOD_JSON,status=200)
        except Exception as error:
            ERROR_JSON["reason"]=str(error)
            print(ERROR_JSON)
            return JsonResponse (ERROR_JSON,status=400) 






