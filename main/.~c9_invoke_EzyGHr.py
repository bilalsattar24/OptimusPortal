from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import *


# Create your views here.
# these method names are called when you visit /methodname(request) [i.e website.com/index]

def index(request):
    allEmployees = Employee.objects.all()
    template = loader.get_template('main/index.html') #select html file
    
    trucks = Truck.objects.all()
    
    # dictionary that can be passed into html file to access variables
    context = {
        'test': "Bilal",
        'trucks' : trucks
    }
    
    return HttpResponse(template.render(context, request))

def newweek(request):
    template = loader.get_template('main/newweek.html')
    trucks = Truck.objects.all()
    # for truck in trucks:
        # print truck.truckName
    context = {
        'test': "Bilal",
        'trucks' : trucks
    }
    return HttpResponse(template.render(context, request))

def day(request):
    template = loader.get_template('main/day.html')
    month = request.GET.get('month')
    day = request.GET.get('day')
    year = request.GET.get('year')
    truckID = request.GET.get('truckID')
    
    trucks = Truck.objects.all()
    truck = None        
    for t in trucks:
        if str(t.id) == str(truckID):
            print "truck found"
            truck = t
            break
    
    #d ate requested from user built to match column in "day" object
    requestedDate = year + "-" + month + "-" + day
    
    # get all days
    days = Day.objects.all()
    day = None # this day will be passed into index.html
    
    
    for d in days:
        if str(d.date) == requestedDate:
            day = d
            break
    
    if not day:
        print "day not found"
    
    employees = Employee.objects.all()
    stores = Store.objects.all()
    
    # python dictionary to be passed into day.html    
    context = {
        'month' : month,
        'day' : day,
        'truck' : truck,
        'employees' : employees,
        'stores' : stores
    }
    
    if day:
        context['dayDate'] = str(day.date)
        context['dayID'] = str(day.id)
    
    return HttpResponse(template.render(context, request))

def addday(request):
    template = loader.get_template('main/day.html')
    dayID = request.GET.get('dayID')
    day
    date = request.GET.get('datePick')
    numDeliveries = request.GET.get('numDeliveries')
    helper = request.GET.get('helperName')
    driver = request.GET.get('driverName')
    storeNum = request.GET.get('storeNum')
    saturdayDate = request.GET.get('saturdayDate')
    
    
    print driver
    
    
    days = Day.objects.all()

    if dayID:
        for d in days:
            if str(d.id) == str(dayID):
    #            d.dayName = dayName
    #            d.date = date
    #            d.numDeliveries = numDeliveries
    #            d.helper = helper
    #            d.driver = driver
    #            d.storeNum = storeNum
    #            # d.saturday = saturdayDate
    #            d.save()
    #            break
    
    
                
    
    return HttpResponse(template.render(request))