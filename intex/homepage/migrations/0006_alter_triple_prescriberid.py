# Generated by Django 3.2.9 on 2021-12-04 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20211204_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triple',
            name='prescriberid',
            field=models.IntegerField(),
        ),
    ]
