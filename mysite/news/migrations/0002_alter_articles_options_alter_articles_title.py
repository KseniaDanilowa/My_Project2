# Generated by Django 4.2.1 on 2023-06-09 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
    ]
