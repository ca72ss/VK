from django.db import models

class Person(models.Model):
    person_name = models.TextField()
    person_photo = models.TextField()

    def search(self):
        self.save()
