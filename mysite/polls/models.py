from django.db import models


class Feedback(models.Model):
    email = models.CharField(max_length=100)
    text = models.TextField()