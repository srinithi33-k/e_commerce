from e_commerce_apis.source.common.common_utils import cursor_creater,token_validator
from e_commerce_apis.source.common.query_constants import FETCH_USER_Picture_DETAILS  
from jwt import decode
from e_commerce_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from django.http import JsonResponse
from json import loads



class GetUserpictureDetails:
    @staticmethod
    def get_user_picture_details(request):
        try:
            sample_dict=loads(request.body)
            # sample_dict={"user_id":5001,"product_id":13008}
            if not token_validator(request.headers.get("Authorization"),sample_dict.get("user_id")):
                raise Exception("invalid user!")
            connect,cursor=cursor_creater()
            field=sample_dict.get("product_id"),
            query=FETCH_USER_Picture_DETAILS  % field
            cursor.execute(query)
            record = cursor.fetchall()
            
            GOOD_JSON["data"]=str(record)
            # print(GOOD_JSON)
            return JsonResponse(GOOD_JSON,status=200)
               
                
        except Exception as error:
            ERROR_JSON["reason"] =str( error)
            # print(ERROR_JSON)  
            return JsonResponse(ERROR_JSON,status=400)  
            