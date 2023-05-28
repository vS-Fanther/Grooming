"""
URL configuration for Grooming project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from project.views import index, services, contact, sign_in, sign_up, contact_us, profile, edit_profile, leave_account, \
    book_appointment

urlpatterns = [
    path('', index, name='index'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('contact_us/', contact_us, name='contact_us'),
    path('profile/', profile, name='profile'),
    path('leave_account/', leave_account, name='leave_account'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('book_appointment/', book_appointment, name='book_appointment'),
]
