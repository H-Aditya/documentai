# Generated by Django 3.1.1 on 2020-09-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_mytrainedmodel_model_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytrainedmodel',
            name='model_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
