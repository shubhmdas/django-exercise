from django.urls import path
from .views import *

urlpatterns = [
    path('messages/', createMessage, name='create-message'),
]