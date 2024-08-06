from django.urls import path
from .views import users_list, register

urlpatterns = [
    path('', users_list, name='users'),

]
