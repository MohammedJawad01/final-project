# Generated by Django 4.2.5 on 2023-09-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='picture',
            field=models.ImageField(null=True, upload_to='rooms/'),
        ),
    ]