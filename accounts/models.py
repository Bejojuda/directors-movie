from django.db import models
from django.conf import settings

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Thriller', 'Thriller'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
        ('Mystery', 'Mystery'),
        ('Sci-fic', 'Sci-fic')
    ]
    name = models.CharField(max_length=30)
    duration = models.DurationField()
    genre = models.CharField(max_length=40, choices=GENRE_CHOICES, default='Action')
    description = models.TextField()

    # 'auth.user' permite el uso de la clase User al momento de crear el serializer
    # related_name es el nombre colocado en el fields
    # director = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    # settigs.AUTH_USER_MODEL referencia al usuario autenticado actualmente
    director = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
