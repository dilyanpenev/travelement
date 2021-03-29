from django.db import models


class Post(models.Model):
    title = models.TextField()
    pub_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title
