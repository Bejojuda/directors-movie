from django.contrib.auth.models import User
from .models import Movie
from .serializers import DirectorSerializer, MovieSerializer

from rest_framework.response import Response            # Permite responder al cliente
from rest_framework import status
from rest_framework.views import APIView
# GENERIC VIEWS
from rest_framework import generics                     # Generic Views
from rest_framework import mixins                       # Mixins proporcionan metodos básicos de comportamiento de las views 

from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsSelfOrReadOnly

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


class DirectorView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = DirectorSerializer            # El serializer utilizado para la validación, envio y recepción de data

    queryset = User.objects.all()                # El query set determina las instancias de qué modelo van a ser utilizadas en la Generic View

    
    # authentication_classes = [SessionAuthentication, BasicAuthentication]         # Autentificación básica (login)
                                                                                    # 
    #authentication_classes = [TokenAuthentication]                                  # Autentificación con token
    #permission_classes = [IsAuthenticated]                                          #

    def get(self, request):
        return self.list(request)               # .list() crea una lista a partir de un queryset

    def post(self, request):
        return self.create(request)

class DirectorDetailsView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]#, IsSelfOrReadOnly]
    serializer_class = DirectorSerializer

    queryset = User.objects.all()

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)



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