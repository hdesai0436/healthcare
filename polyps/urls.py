from django.urls import path
from . import views

urlpatterns = [
    path('',views.polyps_predication, name='polyps_predication')
]