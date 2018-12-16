from django.http.response import HttpResponse
from . import wrapper


def welcome(request):
    return HttpResponse(content=b"welcome")


def callback(request, system, status):
    
    if status == 'success':
        fn = wrapper.get_success_callback_function_for(system)
        if fn is not None:
            val = fn(request.POST)
        
    elif status == 'failure':
        fn = wrapper.get_failure_callback_function_for(system)
        if fn is not None:
            val = fn(request.POST)
        
    return HttpResponse(content=b"ok")