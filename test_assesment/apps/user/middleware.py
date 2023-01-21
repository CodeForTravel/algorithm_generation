from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.urls import resolve


class TokenValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.whitelist = ["login", "register", "forget-password", "reset-password"]


    def __call__(self, request):
        access_token = request.headers.get('Authorization')
        if resolve(request.path_info).url_name not in self.whitelist:
            if access_token:
                try:
                    token = Token.objects.get(key=access_token)
                    if token.user:
                        request.user = token.user
                    else:
                        return JsonResponse({'error': 'Invalid token'}, status=401)
                except Token.DoesNotExist:
                    return JsonResponse({'error': 'Invalid token'}, status=401)
            else:
                return JsonResponse({'error': 'Token not provided'}, status=401)
        response = self.get_response(request)
        return response



