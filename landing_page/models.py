from django.db import models


# Create your models here.


class Landing(models.Model):
    username = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    url = models.URLField()

    def __str__(self):
        return f"{self.username}  {self.name}  {self.url}"
