from rest_framework import serializers
from .models import *



class MovieSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.ReadOnlyField(source='director.username')

    class Meta:
        model = Movie
    
        fields = ['url', 'name', 'director', 'duration', 'genre', 'description']

'''


# MODEL SERIALIZER

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director

        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie

        fields = '__all__'

'''