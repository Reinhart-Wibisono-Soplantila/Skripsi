# myapp/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user is authenticated and not in the exempt URLs
        if not request.user.is_authenticated:
            if not request.path.startswith('/login/') and not request.path.startswith('/static/'):
                return redirect('app_user:login')  # Adjust to your login URL name
        response = self.get_response(request)
        return response
