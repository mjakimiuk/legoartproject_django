from django.db import models
import os

class ArtProject(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='art/img')

    def __str__(self):
        return self.title

    def filename(self):
        return os.path.basename(self.img.name)