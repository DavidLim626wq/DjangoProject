# Generated by Django 2.2 on 2019-11-03 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191103_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='191103082851', editable=False, max_length=140),
        ),
    ]