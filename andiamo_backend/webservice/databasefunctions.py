from webservice.models import *

import hashlib

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
