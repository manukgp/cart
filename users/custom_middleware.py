from django.shortcuts import reverse,redirect
from django.http import HttpResponseForbidden

class RestrictAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_urls = ['/login/', '/register/',]

        print(request)
        print(request.path, request.user.is_authenticated)
        if not request.user.is_authenticated and request.path not in allowed_urls:
            print(request.user.is_authenticated)
            return redirect('/login/')
            # return HttpResponseForbidden("Access denied. You are not allowed to access this page.")
        
        response = self.get_response(request)
        return response
