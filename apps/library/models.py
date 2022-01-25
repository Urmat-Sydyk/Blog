from django.db import models

from django.db import models


class BookGenre(models.Model):
    title = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(to=BookGenre, on_delete=models.CASCADE, related_name='Book')



