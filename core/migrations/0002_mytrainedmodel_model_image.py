# Generated by Django 3.1.1 on 2020-09-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytrainedmodel',
            name='model_image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
