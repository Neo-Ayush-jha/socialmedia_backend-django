# Generated by Django 4.1.5 on 2023-01-30 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myInstagram', '0002_account_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]