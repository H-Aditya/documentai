# Generated by Django 3.1.1 on 2020-09-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200909_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytrainedmodel',
            name='model_image',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
