# Generated by Django 3.2.9 on 2021-12-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='drugId',
            field=models.IntegerField(),
        ),
    ]