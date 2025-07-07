from django.shortcuts import render,redirect
from . forms import CreateUserForm
# from  django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def home(request):
    return render(request, 'account/index.html')
    

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = CreateUserForm()
    
    # Ensure context is defined for both GET and POST
    context = {"registerForm": form}

    return render(request, 'account/register.html', context)
    

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') # Get the username/email from the form
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_writer:  # Check if the user is a writer
                # If the user is authenticated, log them in and redirect to the index page
                login(request, user)
                return redirect('writer_dashboard')  # Redirect to the writer dashboard
            if user is not None and not user.is_writer:
                # If the user is authenticated but not a writer, redirect to a different page or show an error
                login(request, user)
                return redirect('client_dashboard') # Redirect to index or another page for non-writer users
    else:   
    # If the user is already authenticated, redirect to the home page
        if request.user.is_authenticated and user.is_writer:
            return redirect("writer_dashboard")
        if request.user.is_authenticated and not user.is_writer:
            return redirect("client_dashboard")
    form = AuthenticationForm()
    context = {"loginForm": form}
    # If the user is not authenticated, render the login page
    return render(request, 'account/user-login.html', context)


def user_logout(request):
    """
    Log out the user and redirect to the home page.
    """
    logout(request)
    return redirect('home')  # Redirect to the home page after logout   


def privacy_policy(request):
    """
    Render the privacy policy page.
    """
    return render(request, 'terms/privacy_policy.html')

def terms_of_service(request):
    """
    Render the terms of service page.
    """
    return render(request, 'terms/terms_of_service.html')

def contact_us(request):
    """
    Render the contact us page.
    """
    return render(request, 'terms/contact_us.html')
def about_us(request):
    """ 
    Render the about us page.
    """
    return render(request, 'terms/about_us.html')
