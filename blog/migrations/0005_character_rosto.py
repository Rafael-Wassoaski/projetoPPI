# Generated by Django 2.0.13 on 2019-04-21 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_character_rosto'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='rosto',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
