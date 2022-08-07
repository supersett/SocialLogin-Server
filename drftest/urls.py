from django.contrib import admin
from django.urls import path
from .views import CoordinateCreateAPIView,CoordinateDetatilAPIView

urlpatterns = [
    path("coordination/", CoordinateCreateAPIView, name='coordination-list'),
    path("coordination/<int:pk>", CoordinateDetatilAPIView, name='coordination-detail')
]