# Generated by Django 2.2 on 2019-11-03 01:34

from django.db import migrations, models
from blog.models import Post
from django.utils.text import slugify


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20191103_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]