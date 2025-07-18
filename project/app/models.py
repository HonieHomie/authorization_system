from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_logged = models.BooleanField(default=False)

    def __str__(self):
        return self.username
