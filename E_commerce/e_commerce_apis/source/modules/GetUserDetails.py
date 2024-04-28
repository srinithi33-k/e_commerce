from e_commerce_apis.source.common.common_utils import is_email,cursor_creater,token_validator
from e_commerce_apis.source.common.query_constants import FETCH_SELECT_USERS
from jwt import decode
from e_commerce_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from django.http import JsonResponse
from json import loads

class GetUserDetails:
    @staticmethod
    def get_user_details(request):
        try:
            sample_dict=loads(request.body)
            # sample_dict={"email":"srinithi33.k@gmail.com"}
            if not is_email(sample_dict["email"]):
                raise Exception ("invalid email")
            if not token_validator(request.headers.get("Authorization"),sample_dict.get("email")):
                raise Exception("invalid user!")
            connect,cursor=cursor_creater()
            field=sample_dict.get("email"),
            query=FETCH_SELECT_USERS % field
            cursor.execute(query)
            
            record = cursor.fetchall()
            if len(record) == 1:
                GOOD_JSON["data"]=str(record)
                # print(GOOD_JSON)
                return JsonResponse(GOOD_JSON,status=200)
            else:
                raise Exception("Invalid emailid!")      
                
        except Exception as error:
            # print( error) 
            return JsonResponse(ERROR_JSON,status=400)   
            


