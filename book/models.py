from django.db import models
from account.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)
    books = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Genre(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=3)
    def __str__(self):
        return self.title

class FavouriteAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    created = models.DateTimeField(auto_now_add=True)
