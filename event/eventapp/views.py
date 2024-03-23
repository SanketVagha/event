from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from datetime import datetime

# Create your views here.

def index(request):
    data = {}
    return HttpResponse("Hello World!")
@csrf_exempt
def getevent(request):
    data = {}

    if request.method == "POST":
        request_data = JSONParser().parse(request)
        if not 'events' in request_data:
            data['message'] = "Events Required"
            return JsonResponse(data = data, safe= False)
        if not 'latitude' in request_data['events']:
            data['message'] = "Customer latitude Required"
            return JsonResponse(data= data, safe= False)
        if not 'longitude' in request_data['events']:
            data['message'] = "Customer Longitude Required"
            return JsonResponse(data=data, safe= False)
        if not 'date' in request_data['events']:
            data['message'] = "Date Required"
            return JsonResponse(data= data, safe= False)
        offset = 0
        limit = 0
        if  'page' in request_data:
            offset = int(request_data['events']['page'])
        if  'pageSize' in request_data:
            limit = int(request_data['events']['pageSize'])

        offset = (offset * limit) + 1
        limit = (offset + limit) + 1

    return JsonResponse(data= data, safe= False)