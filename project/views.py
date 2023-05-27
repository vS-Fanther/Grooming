from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from project.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def sign_up(request):
    if request.method == 'POST':
        register_user(request)

        return redirect('index')

    return render(request, 'sign-up.html')


def sign_in(request):
    auth_user(request)


def add_service(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        print(name, price)

        return redirect('index')

    return render(request, 'add-service.html')


def contact_us(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        print(name, email, message, phone)

        return redirect('contact')

    return render(request, 'sign-in.html')


def register_user(request):
    email = request.POST.get('email')
    exists = User.objects.filter(email=email).exists()
    if exists:
        render(request, 'sign-up.html')

    user = User(
        name=request.POST.get('name'),
        email=request.POST.get('email'),
        password=make_password(request.POST.get('password')),
        phone_number=request.POST.get('phone'),
        age=request.POST.get('age'),
        breed=request.POST.get('breed'),
    )
    user.is_admin = False
    print(user)
    user.save()


def auth_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('sign_in')
    else:
        return render(request, 'sign-in.html')
