from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name='indexenglish'),
    path('contact', contact ,name='contact'),
    path('applications/', views.ApplicationsView.as_view(), name='applications'),
]