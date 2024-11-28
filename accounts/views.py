from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)  # Inicia sesión automáticamente después del registro
                return redirect('index')
            except:
                messages.error(request, 'El nombre de usuario ya existe.')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
    return render(request, 'signup.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login.html')  # Redirige al login después de cerrar sesión

