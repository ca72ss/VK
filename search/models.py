from django.db import models
from django.utils import timezone

class Person(models.Model):
    person_name = models.CharField(max_length=200)
    person_photo = models.TextField()

    def __str__(self):
        return self.person_name
