from .serializers import DirectorSerializer
from .permissions import IsSelfOrReadOnly
from .models import Director

from django.contrib.auth.models import User
from rest_framework import generics                     # Generic Views
from rest_framework import mixins 
from rest_framework import permissions

from django.contrib.auth.hashers import make_password

class DirectorView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = DirectorSerializer            # El serializer utilizado para la validación, envio y recepción de data

    queryset = Director.objects.all()                # El query set determina las instancias de qué modelo van a ser utilizadas en la Generic View


    def get(self, request):
        return self.list(request)               # .list() crea una lista a partir de un queryset

    def post(self, request):
       return self.create(request)

        
    def perform_create(self, serializer):
        return Director.objects.create_user(**serializer.validated_data)

class DirectorDetailsView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]#, IsSelfOrReadOnly]
    serializer_class = DirectorSerializer

    queryset = Director.objects.all()

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)