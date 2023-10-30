from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Bookings,Food,FoodBookings,Train
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Food)
admin.site.register(FoodBookings)
admin.site.register(Bookings)
admin.site.register(Train)