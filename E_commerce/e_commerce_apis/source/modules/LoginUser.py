from e_commerce_apis.source.common.common_utils import cursor_creater
from base64 import b64decode
from e_commerce_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from jwt import encode
from json import loads
from django.http import JsonResponse
from e_commerce_apis.source.common.query_constants import FETCH_LOGIN_USERS
from json import loads


class LoginUser:
    @staticmethod
    def login_user(request):
        try:
            # sample_dict={"email":"srinithi33.k@gmail.com","password":"P4r1ty@sri"}
            sample_dict=loads(request.body)
            # sample_dict={key:"'"+ value +"'" for key,value in sample_dict.items()}
            field=(sample_dict.get("email"),)
            select_query = FETCH_LOGIN_USERS % field
            connect,cursor=cursor_creater()
            cursor.execute(select_query)
            record=cursor.fetchall()
            
            if len(record) == 1:
                result_dict = record[0]
                result_dict["created_on"] = result_dict.get('created_on').strftime('%Y-%m-%d %H:%M:%S')
                result_dict["modified_on"] = result_dict.get('modified_on').strftime('%Y-%m-%d %H:%M:%S')
                decoded_crtpassword = b64decode(result_dict.get("password")).decode()
                if decoded_crtpassword==sample_dict.get("password"):
                    token=encode(result_dict,'uoqdoolW0ZPOBI_qGNjpXnlpAPW3iNi3rS3_9NL36xo',algorithm='HS256')
                    GOOD_JSON["token"]=token
                    GOOD_JSON["user_id"]=result_dict["id"]
                    # print(GOOD_JSON)
                    return JsonResponse(GOOD_JSON,status=200)
                else:
                    raise Exception("Invalid reg_no or password!")   
        
            else:
                raise Exception("user does not exist! try to signup")        
        except Exception as error:
            ERROR_JSON["reason"]=str(error)
            # print(ERROR_JSON)
            return JsonResponse (ERROR_JSON,status=400)   
        
        