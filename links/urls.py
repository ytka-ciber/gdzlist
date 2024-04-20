from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('hub/', views.links_hub, name='links_hub'),
]
