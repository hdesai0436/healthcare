from django.urls import path
from . import views

urlpatterns = [
    
    path('alz_predication/', views.alz_pred, name='alz_predication')
]