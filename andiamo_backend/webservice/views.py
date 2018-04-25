from django.http import HttpResponse, JsonResponse


def index(request):
    data = {"Hello":"World"}
    return JsonResponse(data)

def login(request):
    data = {"End":"Login"}
    return JsonResponse(data)

def register(request):
    data = {"End":"Register"}
    return JsonResponse(data)

def store_locations(request):
    data = {"End":"Store Locations"}
    return JsonResponse(data)

def place_order(request):
    data = {"End":"Place Order"}
    return JsonResponse(data)
