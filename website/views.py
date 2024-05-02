from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    # Check to see if looging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged In !')
            return redirect('website:home')
        else:
            messages.error(
                request, 'There Was An Error Logging In, Please Try Again')
            return redirect('website:home')
    else:
        return render(request, 'website/home.html', {})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Logged Out')
    return redirect('website:home')


def register_user(request):
    return render(request, 'website/register.html', {})
