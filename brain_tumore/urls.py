from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brain/pred/', views.simple_upload, name='brain_predict')
]