from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="user_login")
def client_dashboard(request):
    """
    Render the home page for the client.
    """
    return render(request, "client/dashboard.html")

@login_required(login_url="user_login")
def client_profile(request):
    """
    Render the profile page for the client.
    """
    user = request.user
    context = {
        'user': user,
    }
    return render(request, "client/profile.html", context)