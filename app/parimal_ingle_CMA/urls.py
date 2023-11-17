from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('addContact', views.addContact, name='addContact'),
    path('details', views.details, name='details'),
    path('update', views.update, name='update'),
]
