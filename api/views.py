from multiprocessing import Event
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import EventDetails

# Create your views here.

def createevent(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES
        image = files.get("e_image")

        e = EventDetails()
        e.name = data['e_name']
        e.venue = data['e_venue']
        e.date = data['e_date']
        e.time = data['e_time']
        e.cover_image = image
        e.email = data['e_email']
        e.created_at = data['e_created_at']

        e.save()

        return HttpResponse("Event Created", status = 201)
    else:
        return HttpResponseNotAllowed("POST")

def printevents(request):
    if request.method == 'GET':
        data = list(EventDetails.objects.values_list())
        return JsonResponse(data, safe = False)
    else:
        return HttpResponseNotAllowed("GET")

def printeventsbyyear(request, year):
    if request.method == 'GET':
        data = list(EventDetails.objects.filter(date__year = year).values_list())
        return JsonResponse(data, safe = False)
    else:
        return HttpResponseNotAllowed("GET")

def deletevent(request, id):
    if request.method == 'DELETE':
        try:
            event = EventDetails.objects.get(id = id)
            event.delete()
            return HttpResponse("Event Deleted", status = 202)
        except:
            return HttpResponseNotFound()
    else:
        return HttpResponseNotAllowed("POST")