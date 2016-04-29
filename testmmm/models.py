from django.db import models

# Create your models here.
from django.db import models

class MyModel(models.Model):
    stuff = models.ManyToManyField('self', related_name = 'stuffre', symmetrical=False, blank = True, null = True, verbose_name = "description")

    def __str__(self):
        return "MyModel%i" % self.id