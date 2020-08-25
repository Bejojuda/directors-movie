from django.contrib import admin
from django.urls import path, include
from .views import MovieView, MovieDetailsView, api_root

urlpatterns = [
    path('', MovieView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailsView.as_view(), name='movie-detail'),
]
