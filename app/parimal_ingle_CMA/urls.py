from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('addContact', views.addContact, name='addContact'),
    path('details/<contact_id>', views.details, name='details'),
    path('update/<contact_id>', views.update, name='update'),
    path('deleteConf/<contact_id>', views.deleteConf, name='deleteConf'),
    path('delete/<contact_id>', views.delete, name='delete')
]
