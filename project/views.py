from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        # todo implementation

        return redirect('index')

    return render(request, 'sign-up.html')


def sign_in(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        # todo implementation

        return redirect('index')

    return render(request, 'sign-in.html')
