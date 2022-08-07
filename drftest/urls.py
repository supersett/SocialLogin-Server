from django.contrib import admin
from django.urls import path
from .views import CoordinateCreateAPIView,CoordinateDetatilAPIView

urlpatterns = [
    path("coordination/", CoordinateCreateAPIView.as_view(), name='CoordinateCreateAPIView'),
    path("coordination/<int:pk>", CoordinateDetatilAPIView.as_view(), name='CoordinateDetatilAPIView')
]