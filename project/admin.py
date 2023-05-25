from django.contrib import admin
from project.models import Appointment, Service, User, ContactMessage

admin.site.register(Appointment)
admin.site.register(User)
admin.site.register(Service)
admin.site.register(ContactMessage)
