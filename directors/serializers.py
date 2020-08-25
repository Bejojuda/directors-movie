from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# HYPERLINK

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)

    # Se agrega para poder manejar contraseñas entre los directores
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        
        fields = ['url', 'id', 'username', 'password', 'movies']
    
    # Sobreescribe el create para hacer el hash adecuado a la contraseña
    # def create(self, validated_data):
    #    validated_data['password'] = make_password(validated_data.get('password'))
    #    return super(DirectorSerializer, self).create(validated_data)
    
    
    # Sobreescribe el update para hacer el hash adecuado a la contraseña
    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
