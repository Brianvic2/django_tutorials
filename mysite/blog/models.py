from django.db import models

# Create your models here.
# models.Modelinherits from Model


class Post(models.Model):
    title = models.CharField(max_length=140)  # column name =tabel.datatype(constraint)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
