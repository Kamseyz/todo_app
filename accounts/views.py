from django.shortcuts import render,redirect
from .forms import Login, Registration
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
        user = authenticate(username = email, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Account logged in successfully')
            return redirect('task')
        else:
            messages.error('Invalid credentials')
    else:
        form = Login()       
    return render(request, 'login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Account was created successfully')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')
    else:
        form = Registration()

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


