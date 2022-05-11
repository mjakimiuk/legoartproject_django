from django.db import models

# Create your models here.
class Upload(models.Model):
    filename = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.filename

class File(models.Model):
    file = models.ForeignKey(Upload,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self) -> str:
        return self.text