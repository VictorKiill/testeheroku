import django.shotcuts umport render, redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')
