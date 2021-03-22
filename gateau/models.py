from django.db import models

class Gateau(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.name
