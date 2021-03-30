from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.TextField()
    pub_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title
