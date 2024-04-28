from e_commerce_apis.source.common.query_constants import FETCH_AREA_DETAILS
from e_commerce_apis.source.common.common_utils import cursor_creater,token_validator
from e_commerce_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from json import loads
from django.http import JsonResponse

class GetAreaDetails:
    @staticmethod
    def get_area_details(request):
        try:
            sample_dict=loads(request.body) 
            # if not token_validator(request.headers.get("Authorization"),sample_dict.get("user_id")):
            #     raise Exception("invalid user!")
            # sample_dict={"user_id":5001,"country_id":2000}
            sample_dict["country_id"]=str(sample_dict["country_id"])
            sample_dict["state_id"]=str(sample_dict["state_id"])
            field=sample_dict["country_id"], sample_dict["state_id"]
            query=FETCH_AREA_DETAILS%field
            connect,cursor=cursor_creater()
            cursor.execute(query)
            record=cursor.fetchall()
            print(record)
            if len(record)==1:
                GOOD_JSON["data"]=record
                # print(GOOD_JSON)
                return JsonResponse(GOOD_JSON,status=200)
            else:
                raise Exception("invalid country")    
        except Exception as error:
            ERROR_JSON["reason"]=error
            # print(ERROR_JSON)
            return JsonResponse(ERROR_JSON,status=400)


        
        