# Generated by Django 3.1.2 on 2020-10-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0004_auto_20201029_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.FilePathField(path='/images'),
        ),
    ]
