from webservice.databasefunctions import *

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import math

AUTHORIZATION_TOKEN = "ZNLhfFrapAOTqjcWrseVne4PBfrHkcYG"

## Endpoint: /login
## Description: Endpoint to recieve login data to login a user
## Method: POST
## Arguements: [email, password]
## Return Structure:
'''
{
    "status" : "Integer",
    "data":{
        "user_id" : "Integer",
        "fname" : "String",
        "lname" : "String"
    }
}
'''
@csrf_exempt
def login(request):
    if request.method != "POST":
        data = {"status":0,
                "data":"Invalid request method"}
        return JsonResponse(data)

    if request.META["HTTP_AUTHORIZATION"] != AUTHORIZATION_TOKEN:
        data = {"status":0,
                "data":"Not authorized"}
        return JsonResponse(data)

    try:
        body = request.POST.dict()
        data = get_user(body['email'], body['password'].encode('utf-8'))
    except Exception as e:
        data = {"status" : 0,
                "data" : "Error: " + str(e)}

    return JsonResponse(data)

## Endpoint: /register
## Description: Endpoint to create a new user account
## Method: POST
## Arguements: [email, password, firstname, lastname]
## Return Structure:
'''
{
    "status" : "Integer",
    "data":{
        "user_id" : "Integer",
        "fname" : "String",
        "lname" : "String"
    }
}
'''
@csrf_exempt
def register(request):
    if request.method != "POST":
        data = {"status":0,
                "data":"Invalid request method"}
        return JsonResponse(data)

    if request.META["HTTP_AUTHORIZATION"] != AUTHORIZATION_TOKEN:
        data = {"status":0,
                "data":"Not authorized"}
        return JsonResponse(data)

    try:
        body = request.POST.dict()
        data = create_user(body['email'], body['password'].encode('utf-8'), body['firstname'], body['lastname'])
    except Exception as e:
        data = {"status" : 0,
                "data" : "Error: " + str(e)}

    return JsonResponse(data)

## Endpoint: /store_locations
## Description: Endpoint to return all the store locations
## Method: GET
## Arguements: []
## Return Structure:
'''
{
    "status" : "Integer",
    "data" : {
        "num_of_locations" : 'Integer',
        "locations" : [
            {
                "latitude" : "float",
                "longitude" : "float"
            }
        ]
    }
}
'''
@csrf_exempt
def store_locations(request):
    if request.method != "GET":
        data = {"status":0,
                "data":"Invalid request method"}
        return JsonResponse(data)

    if request.META["HTTP_AUTHORIZATION"] != AUTHORIZATION_TOKEN:
        data = {"status":0,
                "data":"Not authorized"}
        return JsonResponse(data)

    data = get_store_locations()
    return JsonResponse(data)

## Endpoint: /place_order
## Description: Endpoint to handle placing an order
## Method: POST
## Arguements: [user_id, latitude, longitude, total_cost]
## Return Structure:
'''
{
    "status" : "Integer",
    "data" : {
        "order_number" : "Integer",
        "est_delivery_time" : "Integer"
    }
}
'''
@csrf_exempt
def place_order(request):
    if request.method != "POST":
        data = {"status":0,
                "data":"Invalid request method"}
        return JsonResponse(data)

    if request.META["HTTP_AUTHORIZATION"] != AUTHORIZATION_TOKEN:
        data = {"status":0,
                "data":"Not authorized"}
        return JsonResponse(data)

    try:
        body = request.POST.dict()
        store = find_closest_store(float(body['latitude']), float(body['longitude']))
        delivery_time = calc_est_deliverytime(store['distance'])
        data = create_order(body['total_cost'])
        data['est_delivery_time'] = delivery_time
    except Exception as e:
        data = {"status" : 0,
                "data" : "Error: " + str(e)}

    return JsonResponse(data)

## Endpoint: /get_order
## Description: Endpoint to handle retrieving an order
## Method: POST
## Arguements: [order_number]
## Return Structure:
'''
{
    "status" : "Integer",
    "data" : {
        "order_total" : "Float",
        "timestamp" : "DateTime"
    }
}
'''
@csrf_exempt
def get_order(request):
    if request.method != "POST":
        data = {"status":0,
                "data":"Invalid request method"}
        return JsonResponse(data)

    if request.META["HTTP_AUTHORIZATION"] != AUTHORIZATION_TOKEN:
        data = {"status":0,
                "data":"Not authorized"}
        return JsonResponse(data)
    try:
        body = request.POST.dict()
        data = get_order_data(body['order_number'])
    except Exception as e:
        data = {"status" : 0,
                "data" : "Error: " + str(e)}
    return JsonResponse(data)

def calc_est_deliverytime(dist):
    base = 15
    return math.floor(dist * .78 + 15)