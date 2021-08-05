from django.contrib import admin

# Register your models here.
from profiles.models import Profile
#from .models import Product

admin.site.register(Profile)