# Generated by Django 2.2 on 2019-11-03 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191103_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='191103082503', editable=False, max_length=140),
        ),
    ]
