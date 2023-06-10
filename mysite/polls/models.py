from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=50, default='')
    surname = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=100, default='')
    message = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment