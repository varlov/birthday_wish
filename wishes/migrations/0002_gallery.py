# Generated by Django 3.1.2 on 2020-10-29 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FilePathField(path='/img')),
                ('desc', models.CharField(max_length=60)),
            ],
        ),
    ]