from django.shortcuts import render
import json 
from rest_framework.response import Response
from rest_framework.views import APIView

class resultView(APIView):
    def get(self,request):
        try:
            file_path = 'results.json'
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
            return Response({"data" : data},status=200)
        except:
            return Response({"message" : "No histroy of results "},status=400)