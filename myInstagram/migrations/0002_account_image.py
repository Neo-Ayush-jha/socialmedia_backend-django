# Generated by Django 4.1.5 on 2023-01-25 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myInstagram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]
