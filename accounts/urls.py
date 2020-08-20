from django.contrib import admin
from django.urls import path, include
from .views import DirectorView, DirectorDetailsView, MovieView, MovieDetailsView, api_root
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', api_root),
    path('api-auth/', include('rest_framework.urls')),
    path('directors/', DirectorView.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorDetailsView.as_view(), name='user-detail'),
    path('movies/', MovieView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailsView.as_view(), name='movie-detail'),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view())
]
