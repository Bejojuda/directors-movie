from django.db import models

''''
class Director(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

'''

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Thriller', 'Thriller'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
    ]
    name = models.CharField(max_length=30)
    duration = models.DurationField()
    genre = models.CharField(max_length=40, choices=GENRE_CHOICES, default='Action')
    description = models.TextField()

    # 'auth.user' permite el uso de la clase User al momento de crear el serializer
    # related_name es el nombre colocado en el fields
    director = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
