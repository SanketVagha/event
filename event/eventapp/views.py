from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from datetime import datetime, timedelta
from eventapp.serializers import EventSerializer, UserSerializer
from eventapp.models import Event, User
from .background import Background
import math

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
        
        offset = 1
        limit = 10
        startIndex = 0
        endIndex = 0
        if  'page' in request_data['events'] and request_data['events']['page'] > 0:
            offset = int(request_data['events']['page'])
        else:
            offset = 1

        if  'pageSize' in request_data['events'] and request_data['events']['pageSize'] > 0:
            limit = int(request_data['events']['pageSize'])
        else:
            limit = 10

        startIndex = (offset * limit) - limit
        endIndex = (startIndex + limit)

        # print(startIndex, endIndex)
        after14days = datetime.strptime(request_data['events']['date'], "%Y-%m-%d") + timedelta(days=14)
        # print(after14days.strftime("%Y-%m-%d"))

        data['event'] = Background.querySet_to_dict(Event.objects.filter(date__gte = request_data['events']['date'], date__lte = after14days).values('event_name','city_name','date').order_by('date', 'id') [startIndex:endIndex])

        totalEvent = Event.objects.filter(date__gte = request_data['events']['date'], date__lte = after14days).count()
        data['page'] = offset
        data['pageSize'] = limit
        data['totalEvents'] = totalEvent
        data['totalPages'] = math.ceil(totalEvent/limit)

    return JsonResponse(data= data, safe= False)