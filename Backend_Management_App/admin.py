from django.contrib import admin
from .models import CenterAvailability,CommunityCenter,Booking
# Register your models here.
admin.site.register(CommunityCenter)
admin.site.register(CenterAvailability)
admin.site.register(Booking)