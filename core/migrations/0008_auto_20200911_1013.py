# Generated by Django 3.1.1 on 2020-09-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200910_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytrainedmodel',
            name='model_image',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
