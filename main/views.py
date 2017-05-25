from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import *


# Create your views here.
def index(request):
    allEmployees = Employee.objects.all()
    template = loader.get_template('main/index.html')
    context = {
        'test': "Bilal"
    }
    return HttpResponse(template.render(context, request))

def newweek(request):
    template = loader.get_template('main/newweek.html')
    trucks = Truck.objects.all()
    #for truck in trucks:
        #print truck.truckName
    context = {
        'test': "Bilal",
        'trucks' : trucks
    }
    return HttpResponse(template.render(context, request))

def day(request):
    template = loader.get_template('main/day.html')
    month = request.GET.get('month')
    
    context = {
        'month' : month
    }
    return HttpResponse(template.render(context, request))
    