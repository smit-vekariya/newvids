from django.shortcuts import render
from rest_framework.views import APIView ,View
from rest_framework import viewsets
import requests
from rest_framework.response import Response
from apis.serializers import PosterSerializer, TemplateSerializer
from django.db import transaction
import urllib.request
from apis.models import Poster

# Create your views here.
class AddCatData(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []

    def add_cat(self, request):
        data = {"api_unix": "1714408661", "accessToken": "81aa0be6706e60f0c02f1a9ba12c7f27", "app_type": "ios", "userId": "nV+rYlehns3ah9Q0E9JLUg==", "ver_code": 1.0}
        response = requests.post("https://newvids.xyz/wowstory/ptmkr/explorecategory", data, timeout=10)
        if response.status_code == 200:
            response = response.json()
            if response["msgcode"] == 1:
                for data in response["all_category"]:
                    print(f">>>> Add cat_id ({data['cat_id']})")
                    poster_data ={}
                    poster_data["cat_id"] = data["cat_id"]
                    poster_data["cat_name"] = data["cat_name"]
                    poster_serializer = PosterSerializer(data=poster_data)
                    if poster_serializer.is_valid():
                        poster_instance = poster_serializer.save()
                    else:
                        raise Exception(f"{poster_serializer.errors}")
        return Response("Cat data enter successfully")

    def add_data(self, request):
        poster_data = Poster.objects.values_list("cat_id","id")
        for cat_id in poster_data:
            for pagecode in range(0,40+1):
                print(f"=======================>start cat_id ({cat_id[0]}) of pagecode ({pagecode}) <===========================")
                data ={"search_keyword": "", "pagecode": pagecode, "userId": "nV+rYlehns3ah9Q0E9JLUg==", "api_unix": "1714409109", "cat_id": cat_id[0], "app_type": "ios", "ver_code": 1.0, "accessToken": "81aa0be6706e60f0c02f1a9ba12c7f27"}
                response = requests.post("https://newvids.xyz/wowstory/ptmkr/gettemplatedata", data, timeout=10)
                if response.status_code == 200:
                    response = response.json()
                    if response["msgcode"] == 1:
                        for temp_data in response["template_list"]:
                            templete_data = temp_data
                            templete_data["poster_id"] = cat_id[1]
                            templete_serializers = TemplateSerializer(data=templete_data)
                            if templete_serializers.is_valid():
                                templete_serializers.save()
                            else:
                                raise Exception(f"{templete_serializers.errors}")
                        print(f"=======================>finish cat_id ({cat_id[0]}) of pagecode ({pagecode}) <===========================")
                    else:
                        print(f"==> finish page for cat_id ({cat_id[0]}) at pagecode ({pagecode}) <===========================")
                        break
            break
        return Response("Data enter successfully")

# https://8000-monospace-newvids-1714469996852.cluster-fu5knmr55rd44vy7k7pxk74ams.cloudworkstations.dev/apis/add_cat
# https://8000-monospace-newvids-1714469996852.cluster-fu5knmr55rd44vy7k7pxk74ams.cloudworkstations.dev/apis/add_data



# class AddData(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request):
#         for i in range(49,50+1):
#             print(f"======================= >start page number ({i}) <===========================")
#             data = {"userId": "Y1eID7Cv00d4amwRQWrMAQ==", "app_type": "ios", "pagecode": i, "ver_code": 1.0, "accessToken": "910dfdfda1a3c2153008551a55327cd0", "api_unix": "1713807882"}
#             response = requests.post("https://newvids.xyz/wowstory/ptmkr/posterdata", data, timeout=10)
#             if response.status_code == 200:
#                 response = response.json()
#                 print("response", response)
#                 if response["msgcode"] == 1:
#                     for data in response["poster_data"]:
#                         print(f">>>> start cat_id ({data['cat_id']}) on page ({i})")
#                         poster_data ={}
#                         poster_data["cat_id"] = data["cat_id"]
#                         poster_data["cat_name"] = data["cat_name"]
#                         poster_serializer = PosterSerializer(data=poster_data)
#                         if poster_serializer.is_valid():
#                             poster_instance = poster_serializer.save()
#                         else:
#                             raise Exception(f"{poster_serializer.errors}")
#                         for temp_data  in data["template_data"]:
#                             templete_data = temp_data
#                             templete_data["poster_id"] = poster_instance.id
#                             templete_serializers = TemplateSerializer(data=templete_data)
#                             if templete_serializers.is_valid():
#                                 templete_serializers.save()
#                             else:
#                                 raise Exception(f"{templete_serializers.errors}")
#                 else:
#                     return Response(f"Something went wrong. msgcode getting {response['msgcode']}.")
#             else:
#                 return Response("Something went wrong while getting data from newvids!")
#             print(f"======================= >finish page number ({i}) <===========================")
#         return Response("Data enter successfully")

# https://8000-monospace-newvids-1713848878294.cluster-7ubberrabzh4qqy2g4z7wgxuw2.cloudworkstations.dev/apis/add_data
# http://192.168.29.175:8000/apis/add_data


# https://newvids.xyz/wowstory/ptmkr/explorecategory
# ["api_unix": "1714408661", "accessToken": 81aa0be6706e60f0c02f1a9ba12c7f27, "app_type": "ios", "userId": nV+rYlehns3ah9Q0E9JLUg==, "ver_code": 1.0]

# https://newvids.xyz/wowstory/ptmkr/gettemplatedata
# ["search_keyword": , "pagecode": 0, "userId": nV+rYlehns3ah9Q0E9JLUg==, "api_unix": "1714409109", "cat_id": 339, "app_type": "ios", "ver_code": 1.0, "accessToken": 81aa0be6706e60f0c02f1a9ba12c7f27]