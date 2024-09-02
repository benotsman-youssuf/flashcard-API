from django.db import models

# Create your models here.

class Flashcards(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    def __str__(self):
        return self.question
    

