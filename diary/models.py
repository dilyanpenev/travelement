from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PostManager(models.Manager):
    def create_post(self, title, user, desc):
        post = self.create(title=title, pub_date=timezone.now(),
                           user=user, description=desc)
        return post


class Post(models.Model):
    title = models.TextField()
    pub_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()

    objects = PostManager()

    def __str__(self):
        return self.title
