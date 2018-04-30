from webservice.models import *

import hashlib
import math

# checks if the user already exists. If not, attempt to create the user
# and return the information to the view
def create_user(email, password, firstname, lastname):
    if User.objects.filter(email=email).first() is not None:
        return {
            "status" : 0,
            "data" : "User already exists"
        }

    try:
        # hash the password before inserting
        hashed = hashlib.sha512(password).hexdigest()
        user = User(email=email, password=hashed, fname=firstname, lname=lastname)
        user.save()
    except Exception as e:
        return {
            "status" : 0,
            "data" : str(e)
        }

    return {
        "status" : 1,
        "data" : {
            "user_id" : user.user_id,
            "firstname" : user.fname,
            "lastname" : user.lname
        }
    }

def get_user(email, password):
    # hash to look up in DB
    hashed = hashlib.sha512(password).hexdigest()
    user = User.objects.filter(email=email, password=hashed).first()
    if user is None:
        return {
            "status" : 0,
            "data" : "User does not exist"
        }
    return {
        "status" : 1,
        "data" : {
            "user_id" : user.user_id,
            "firstname" : user.fname,
            "lastname" : user.lname
        }
    }

def get_store_locations():
    stores = Store.objects.all()
    locations = []
    for i in stores:
        loc = {"store_num" : i.id,
               "latitude" : i.latitude,
               "longitude" : i.longitude}
        locations.append(loc)
    return {
        "status" : 1,
        "data": locations
    }

def create_order(user_id, store_id, total):
    try:
        user = User.objects.filter(user_id=user_id).first()
        store = Store.objects.filter(id=store_id).first()
        order = Order(user=user, store=store, total=total)
        order.save()
    except Exception as e:
        return {"status" : 0,
                "data" : "Error: " + str(e)}

    return {"status" : 1,
            "data": {
                    "order_number":order.id
                    }
            }

def find_closest_store(latitude, longitude):
    stores = Store.objects.all()
    closest = stores[0]
    dShort = calculate_distance(closest.latitude, closest.longitude, latitude, longitude)
    for i in stores:
        currDist = calculate_distance(i.latitude, i.longitude, latitude, longitude)
        if dShort > currDist:
            closest = i
            dShort = currDist

    return {"store_id" : closest.id,
            "distance" : dShort/1000
            }

def calculate_distance(lat1, lon1, lat2, lon2):
    earthRadius = 6371
    dlat = degrees_to_rads(lat2 - lat1)
    dlon = degrees_to_rads(lon2 - lon1)

    lat1 = degrees_to_rads(lat1)
    lat2 = degrees_to_rads(lon2)

    a = math.sin(dlat/2) * math.sin(dlat/2) + math.sin(dlon/2) * math.sin(dlon/2) * math.cos(lat1) * math.cos(lat2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return earthRadius * c



def degrees_to_rads(degrees):
    return degrees * (3.14159/180)
