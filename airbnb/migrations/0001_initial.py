# Generated by Django 3.1.1 on 2020-09-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(choices=[('Palm', 'Plam'), ('Jumerah', 'Jumerah'), ('five', 'five')], max_length=30)),
                ('location', models.CharField(choices=[('Dubai', 'Dubai'), ('London', 'London'), ('Texas', 'Texas')], max_length=30)),
                ('check_in', models.DateTimeField(auto_now_add=True)),
                ('check_out', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]