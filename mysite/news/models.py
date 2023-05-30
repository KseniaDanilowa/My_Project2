from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField('Название', max_length=250)
    content = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


