from django.urls import path
from . import views

urlpatterns = [
    path('', views.Recipes_home, name='Recipes_home'),
    path('create/', views.Recipes_create, name='Recipes_create'),
    path('<int:pk>/details/', views.Recipes_get, name='Recipes_get'),
    path('<int:pk>/edit/', views.Recipes_edit, name='Recipes_edit'),
    path('<int:pk>/delete/', views.Recipes_delete, name='Recipes_delete'),
]
