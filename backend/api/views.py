from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    print(request.GET)
    body = request.body # byte string of JSON data 
    data = {}
    try:
        data= json.loads(body) # takes string of JSON -> Python Dictionary
    except:
        pass

    print(data)
    data['headers'] = dict(request.headers) # newer version of request.META
    data['content_type'] = request.content_type
    return JsonResponse(data)



