from modulefinder import LOAD_CONST
from django.db import models

# Create your models here.

from django.urls import reverse # to create a URL of the right format.

import uuid # For unique film instance
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a film genre(e.g. Science Fiction)")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter here film language (e.g. English)")

    def __str__(self):
        return self.name
    
class Producer(models.Model):
    name = models.CharField(max_length=200, help_text="Enter here to producer of film.")

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=200, help_text="Enter here a name of film")

    actor = models.ForeignKey("Actor", on_delete=models.SET_NULL, null = True) # if without True will do mistakes, One to many 

    description = models.TextField(max_length=1000, help_text="Enter here please some information about film.")

    genre = models.ManyToManyField(Genre, help_text="Select a genre for this film.<a href='https://en.wikipedia.org/wiki/Film_genre'>Genres</a>") # Many to many

    language = models.ManyToManyField(Language, help_text="Select a language for this film.") # Many to many

    producer = models.ManyToManyField(Producer, help_text="Select a producer for this film.")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("film-detail", args=[str(self.id)])

    def display_genre(self):
        return ", ".join(genre.name for genre in self.genre.all())

    display_genre.short_description = "Genre"

    def display_language(self):
        return ", ".join(language.name for language in self.language.all())
    
    display_language.short_description = "Language"

class FilmOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular film across whole catalog")

    film = models.ForeignKey("Film",on_delete=models.RESTRICT, null = True)

    imprint = models.CharField(max_length=200)

    was_watched = models.DateField(null=True, blank=True)

    was_watched_user = models.ForeignKey(User,on_delete = models.SET_NULL, null = True, blank = True)

    LOAN_STATUS = (
        ("w", "Was watched"),
        ("a", "Available"),
        ("m", "Still make"),
        ("r", "Reserved"),
        ("t", "Maintenance"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="t",
        help_text="Film availability"
    )

    class Meta:
        ordering = ["was_watched"]

    def __str__(self):
        return f'{self.id}({self.film.title})'
    
class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField(null = True, blank=True)

    date_of_death = models.DateField("Died", null = True, blank=True)

    some_information = models.TextField(max_length=1000, help_text="Enter here some information about this actor")

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse('actor-detail',args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name},{self.first_name}'
    
    