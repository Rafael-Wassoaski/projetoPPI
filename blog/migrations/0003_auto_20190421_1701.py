# Generated by Django 2.0.13 on 2019-04-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190421_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='rosto',
            field=models.ImageField(upload_to='images'),
        ),
    ]
