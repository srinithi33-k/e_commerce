from e_commerce_apis.source.common.common_utils import is_password,is_email
# from psycopg2 import IntegrityError
from e_commerce_apis.source.common.common_utils import cursor_creater
from e_commerce_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from base64 import b64encode
from e_commerce_apis.source.common.query_constants import insert_query_marker
from json import loads
from django.http import JsonResponse
from datetime import datetime
from mysql.connector import IntegrityError
from jwt import decode

class RegisterUser:
    @staticmethod
    def register_user(request):
        try:
            # sample_dict={"name":"srinithi","mobile_number":8220834963,"password":"P4r1ty@sri","email":"srinithi33.k@gmail.com","country_id":2000}
            
            # print(sample_dict)
            sample_dict=loads(request.body)
            if not is_email(sample_dict.get("email")):
                raise Exception("invalid email")
            if not is_password(sample_dict.get("password")):
                raise Exception("invalid password")
            sample_dict["created_on"]=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sample_dict["modified_on"]=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sample_dict["status"]="active"
            sample_dict["created_by"]="system"
            sample_dict["modified_by"]="system"
            sample_dict["country_id"]=str(sample_dict.get("country_id"))
            sample_dict["mobile_number"]=str(sample_dict.get("mobile_number"))
            # print(sample_dict.get("mobile_number"))
            encoded_password =b64encode(sample_dict.get("password").encode()).decode()
            sample_dict["password"]=encoded_password
            connect,cursor = cursor_creater()   
            print(sample_dict)
            sample_dict={key:"'"+ value +"'" for key,value in sample_dict.items()}
            print(sample_dict)
            insert_query=insert_query_marker("user_profile",sample_dict)

            cursor.execute(insert_query)
            connect.commit()
            print(GOOD_JSON)
            return JsonResponse(GOOD_JSON,status=200)
            
        except IntegrityError as error:
            error_message=str(error)
            return JsonResponse(ERROR_JSON,status=400)
        except Exception as error:
            ERROR_JSON["reason"]=error
            print(ERROR_JSON)  
            return JsonResponse(ERROR_JSON,status=400)  
      
