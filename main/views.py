from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from models import *


# Create your views here.
# these methods are called when you visit /methodname(request) [i.e website.com/index]
def home(request):
    #this method is purely to redirect to /main
    template = loader.get_template('main/index.html') #select html file
    context = {
        'test': "Bilal",
        'selectDateTruck': "Select a date and truck"
    }
    return redirect('/main')

def index(request):
    allEmployees = Employee.objects.all()
    template = loader.get_template('main/index.html') #select html file
    
    trucks = Truck.objects.all()
    success = request.GET.get('success')
    # dictionary that can be passed into html file to access variables
    context = {
        'test': "Bilal",
        'trucks' : trucks,
        'selectDateTruck': "Select a date and truck",
        'success' : success
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
    
    # date requested from user built to match column in "day" object
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
        'year' : year,
        'truck' : truck,
        'employees' : employees,
        'stores' : stores,
        'requestedDate' : requestedDate
    }
    
    if day:
        context['dayDate'] = str(day.date)
        context['dayID'] = str(day.id)
        context['saturdayDate'] = str(day.saturday)
    
    return HttpResponse(template.render(context, request))

def addday(request):
    # receive all of the data coming from day.html. if dayID
    # is passed, then it's an edit to an exsiting day, otherwise
    # the information will be passed to a new day object
    template = loader.get_template('main/day.html')
    dayID = request.GET.get('dayID')
    dayName = request.GET.get('dayName')
    date = request.GET.get('datePick')
    numDeliveries = request.GET.get('numDeliveries')
    helper = request.GET.get('helperName')
    driver = request.GET.get('driverName')
    storeNum = request.GET.get('storeNum')
    storeNum2 = int(request.GET.get('storeNum2'))
    saturdayDate = request.GET.get('saturdayDate')
    truckName = request.GET.get('truckName')
    #truckName2 = request.GET.get('truckName2')
    isOff = request.GET.get('isOff')
    
    if isOff:
        d = Day()
        d.isOff = True
        d.date = date
        d.dayName = dayName
        d.truck = truckName
        d.save()
        success = "Off Day successfully added!"
        url = '/main/?success='+success
        return redirect(url)
    
    days = Day.objects.all()
    
    # if ID is passed, then this day exsits and it is being edited. 
    if dayID:
        for d in days:
            if str(d.id) == str(dayID):
                d.dayName = dayName
                d.date = date
                d.numDeliveries = numDeliveries
                d.helper = helper
                d.driver = driver
                d.storeNum = storeNum
                if storeNum2:
                    d.storeNum2 = storeNum2
                d.saturday = saturdayDate
                d.truck = truckName
                d.save()
                break
                return redirect('/main')
    
    # otherwise, create a new day with the related information
    else:
        d = Day()
        d.dayName = dayName
        d.date = date
        d.numDeliveries = numDeliveries
        d.helper = helper
        d.driver = driver
        d.storeNum = storeNum
        if storeNum2:
            d.storeNum2 = storeNum2
        d.saturday = saturdayDate
        d.truck = truckName
        d.save()
    return redirect('/main')

def reports(request):
    template = loader.get_template('main/reports.html')
    weekOf = request.GET.get('reportsDateSearch')
    truckID = request.GET.get('truckID')

    trucks = Truck.objects.all()

    if weekOf and truckID:
        generateReports(str(weekOf), str(truckName))
        #return HttpResponse(template.render(context), request))

    #todo: get parameter request from reports.html and check if they exist. if they do, call method to generate report 
    #modify weekOf to meet the format of django date
    daysOfWeek = []
    days = Day.objects.all()
    for d in days:
        if d.saturday == weekOf:
            daysOfWeek.append(d)
    
    truck = None
    for t in trucks:
        if t.id == 6:
            truck = t
    
    
    #sort by day, start from saturday
    #add sorted list to context

    context = {
        'test' : "Bilal",
        'trucks' : trucks
    }
    return HttpResponse(template.render(context, request))

#***--------------- Helper Methods ----------------***#
def generateReports(weekOf, truckName):
    return null # change to whatever info(context) is needed for the report to be generated. 
    