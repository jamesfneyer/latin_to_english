from django.db import models
from django.utils import timezone


class Word(models.Model):
    latin = models.CharField(max_length=200)
    conjugation = models.CharField(max_length=200)
    parts_of_speech = models.CharField(max_length=13)
    definition = models.TextField()
    english = models.CharField(max_length=200)

    def __str__(self):
        return self.latin
