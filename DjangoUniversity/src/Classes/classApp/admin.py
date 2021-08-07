from django.contrib import admin

# classApp is the folder / app, models is the file, djangoClasses is the class
from classApp.models import djangoClasses

admin.site.register(djangoClasses)