from django.urls import path
from . import views

urlpatterns = [
    path('prescriptions/', views.post_prescription, name='prescriptions'),
]
