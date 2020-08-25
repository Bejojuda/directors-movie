from django.contrib import admin
from django.urls import path, include
from .views import DirectorView, DirectorDetailsView

urlpatterns = [
    path('', DirectorView.as_view(), name='director-list'),
    path('<int:pk>/', DirectorDetailsView.as_view(), name='user-detail'),
]