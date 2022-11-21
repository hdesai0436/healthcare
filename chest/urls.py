from django.urls import path
from . import views

urlpatterns = [
   
    path('pred_chest/', views.chest_predict, name='chest_predict')
]