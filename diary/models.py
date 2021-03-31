from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinLengthValidator


class Post(models.Model):
    title = models.CharField(max_length=60, validators=[
                             MinLengthValidator(1, message='Title has to be 1-60 chars')])
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', args=[self.id])
