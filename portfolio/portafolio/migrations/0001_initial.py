# Generated by Django 4.2.4 on 2023-11-16 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='')),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='portafolio/images', verbose_name='')),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
