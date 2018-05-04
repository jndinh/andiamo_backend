from webservice.databasefunctions import *
from webservice.models import Address
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

import json
import math

AUTHORIZATION_TOKEN = "ZNLhfFrapAOTqjcWrseVne4PBfrHkcYG"
OK = 200
UNAUTHORIZED = 401
BAD_REQUEST = 400


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
@api_view(['POST'])
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
## Arguements: [email, password, fname, lname, street_address, city, state, zip_code, line_number(optional)]
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
@api_view(['POST'])
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
        body = json.loads(request.body)
        fname = body.get('fname', '')
        lname = body.get('lname', '')
        email = body.get('email', '')
        password = body.get('password', '')
        street_address = body.get('street_address', '')
        city = body.get('city', '')
        state = body.get('state', '')
        zip_code = body.get('zip_code', '')

	# Optional parameter
        line_number = body.get('line_number', '')

	# Missing parameters...
        if not fname or not lname or not email or not password or not street_address or not city or not state or not zip_code:
            return JsonResponse({'detail' :  'Missing parameters.', 'status' : 0}, content_type="application/json", status=BAD_REQUEST)

	# Create User
        data = create_user(email, password.encode('utf-8'), fname, lname)

        # Create Address
        if data['status'] == 0:
            return JsonResponse(data, content_type = "application/json", status=BAD_REQUEST)
	
        user = data['user']
        address = Address.objects.create(user=user, street_address=street_address, city=city, state=state, zip_code=zip_code) 

	# Optional parameter
        if line_number:
            address.line_number = line_number
            address.save()

	# Registration done...
        data = {
            "status" : 1,
            "data" : {
                "user_id" : user.user_id,
                "firstname" : user.fname,
                "lastname" : user.lname }  
        }

        return JsonResponse(data, content_type="application/json", status=OK)
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
@api_view(['GET'])
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
@api_view(['POST'])
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
@api_view(['POST'])
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
