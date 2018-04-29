from webservice.databasefunctions import *

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json

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

    body = request.POST.dict()

    data = get_user(body['email'], body['password'].encode('utf-8'))

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

    body = request.POST.dict()

    data = create_user(body['email'], body['password'].encode('utf-8'), body['firstname'], body['lastname'])

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

    data = {"End":"Store Locations"}
    return JsonResponse(data)

## Endpoint: /place_order
## Description: Endpoint to handle placing an order
## Method: POST
## Arguements: [user_id, order?]
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

    data = {"End":"Place Order"}
    return JsonResponse(data)
