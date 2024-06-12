import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView

def save_to_json(result_data:dict):
    file_path = 'results.json'
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            data.append(result_data)

        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)    
        

    except:
        with open(file_path, 'w') as json_file:
            json.dump([result_data], json_file, indent=4)
    

class addView(APIView):
    def get(self,request):
        try:
            first_number = float(request.GET.get('first_number', 0))
            second_number = float(request.GET.get('second_number', 0))
            result = first_number + second_number
            
            data = {
                 "operation": "add",
                "input": [first_number, second_number],
                "result": result
            }
            save_to_json(data)
            return Response({'message': "Success" , 'data': data})
        except Exception as e:
            return Response({'error': e}, status=400)


class subView(APIView):
    def get(self,request):
        try:
            first_number = float(request.GET.get('first_number', 0))
            second_number = float(request.GET.get('second_number', 0))
            result = first_number - second_number
            
            data = {
                 "operation": "subtract",
                "input": [first_number, second_number],
                "result": result
            }
            save_to_json(data)
            return Response({'message': "Success" , 'data': data})
        except Exception as e:
            return Response({'error': e}, status=400)



class divideView(APIView):
    def get(self,request):
        try:
            first_number = float(request.GET.get('first_number', 0))
            second_number = float(request.GET.get('second_number', 0))
            try:
                result = first_number/second_number
            except ZeroDivisionError:
                 return Response({'error': 'ZeroDivisionError'}, status=400)

            data = {
                 "operation": "divide",
                "input": [first_number, second_number],
                "result": result
            }

            save_to_json(data)
            
            return Response({'message': "Success" , 'data': data})
        except Exception as e:
            return Response({'error': e}, status=400)



class multiplyView(APIView):
    def get(self,request):
        try:
            first_number = float(request.GET.get('first_number', 0))
            second_number = float(request.GET.get('second_number', 0))
            result = first_number * second_number
            
            data = {
                 "operation": "multiply",
                "input": [first_number, second_number],
                "result": result
            }
            
            save_to_json(data)
            return Response({'message': "Success" , 'data': data})
        except Exception as e:
            return Response({'error': e}, status=400)
