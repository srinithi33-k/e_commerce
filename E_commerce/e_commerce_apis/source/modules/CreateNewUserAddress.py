from datetime import datetime
from e_commerce_apis.source.common.query_constants import insert_query_marker
from e_commerce_apis.source.common.common_utils import cursor_creater,token_validator
from e_commerce_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from django.http import JsonResponse
from mysql.connector import IntegrityError
from jwt import encode
from json import loads

class CreateNewUserAddress:
    @staticmethod
    def create_new_user_address(request):
        try:
            
            sample_dict=loads(request.body) 
            if not token_validator(request.headers.get("Authorization"),sample_dict.get("user_id")):
                raise Exception("invalid user!")
            # sample_dict={"country_id":2000,"user_id":5001,"area_id":4000,"state_id":3000}
            sample_dict["created_on"]=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sample_dict["modified_on"]=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sample_dict["created_by"]="system"
            sample_dict["modified_by"]="system"
            sample_dict["status"]="Active"
            sample_dict["country_id"]=str(sample_dict.get("country_id"))
            sample_dict["user_id"]=str(sample_dict.get("user_id"))
            sample_dict["state_id"]=str(sample_dict.get("state_id"))
            sample_dict["area_id"]=str(sample_dict.get("area_id"))
            connect,cursor = cursor_creater()   
            sample_dict={key:"'"+ value +"'" for key,value in sample_dict.items()}
            insert_query=insert_query_marker("user_address_management",sample_dict)
            cursor.execute(insert_query)
            connect.commit()
            # print(GOOD_JSON)
            return JsonResponse(GOOD_JSON,status=200)
        except IntegrityError as error:
            error_message=str(error)
            return JsonResponse(ERROR_JSON,status=400)
        except Exception as error:
            ERROR_JSON["reason"]=str(error)
            # print(ERROR_JSON)  
            return JsonResponse(ERROR_JSON,status=400)  
               
            

