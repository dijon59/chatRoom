from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('chat:message-list')

    def __str__(self):
        return self.user.username
