# Generated by Django 3.1.1 on 2020-09-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='check_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='check_out',
            field=models.DateTimeField(),
        ),
    ]