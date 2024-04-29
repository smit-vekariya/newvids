from django.shortcuts import render
from rest_framework.views import APIView ,View
import requests
from rest_framework.response import Response
from apis.serializers import PosterSerializer, TemplateSerializer
from django.db import transaction
import urllib.request

# Create your views here.
class AddData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        for i in range(49,50+1):
            print(f"======================= >start page number ({i}) <===========================")
            data = {"userId": "Y1eID7Cv00d4amwRQWrMAQ==", "app_type": "ios", "pagecode": i, "ver_code": 1.0, "accessToken": "910dfdfda1a3c2153008551a55327cd0", "api_unix": "1713807882"}
            response = requests.post("https://newvids.xyz/wowstory/ptmkr/posterdata", data, timeout=10)
            if response.status_code == 200:
                response = response.json()
                print("response", response)
                if response["msgcode"] == 1:
                    for data in response["poster_data"]:
                        print(f">>>> start cat_id ({data['cat_id']}) on page ({i})")
                        poster_data ={}
                        poster_data["cat_id"] = data["cat_id"]
                        poster_data["cat_name"] = data["cat_name"]
                        poster_serializer = PosterSerializer(data=poster_data)
                        if poster_serializer.is_valid():
                            poster_instance = poster_serializer.save()
                        else:
                            raise Exception(f"{poster_serializer.errors}")
                        for temp_data  in data["template_data"]:
                            templete_data = temp_data
                            templete_data["poster_id"] = poster_instance.id
                            templete_serializers = TemplateSerializer(data=templete_data)
                            if templete_serializers.is_valid():
                                templete_serializers.save()
                            else:
                                raise Exception(f"{templete_serializers.errors}")
                else:
                    return Response(f"Something went wrong. msgcode getting {response['msgcode']}.")
            else:
                return Response("Something went wrong while getting data from newvids!")
            print(f"======================= >finish page number ({i}) <===========================")
        return Response("Data enter successfully")

# https://8000-monospace-newvids-1713848878294.cluster-7ubberrabzh4qqy2g4z7wgxuw2.cloudworkstations.dev/apis/add_data
# http://192.168.29.175:8000/apis/add_data