from django.contrib.auth.models import User
from .models import Movie
from .serializers import MovieSerializer

from rest_framework.response import Response            # Permite responder al cliente
from rest_framework import status
from rest_framework.views import APIView
# GENERIC VIEWS
from rest_framework import generics                     # Generic Views
from rest_framework import mixins                       # Mixins proporcionan metodos básicos de comportamiento de las views 

from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


# Hace el hyperlink de los users y los snippets
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'director-list' el name del path en urls.py
        'Directors': reverse('director-list', request=request, format=format),
        'Movies': reverse('movie-list', request=request, format=format)
    })

class MovieView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    # Solo permite la modificación a usuarios autenticados
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MovieSerializer

    queryset = Movie.objects.all()

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

        
    def perform_create(self, serializer):

        serializer.save(director=self.request.user)


class MovieDetailsView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    # IsOwnerOrReadOnly es una función de permissions.py que solo permite la modificación al owner de la pelicula
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.delete(request, pk)