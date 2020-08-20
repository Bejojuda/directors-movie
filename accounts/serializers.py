from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

# HYPERLINK

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)

    class Meta:
        model = User
        
        fields = ['url', 'id', 'username', 'movies']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.ReadOnlyField(source='owner.username')

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