# Generated by Django 4.2.1 on 2023-06-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_articles_options_alter_articles_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='img',
            field=models.URLField(default=''),
        ),
    ]
