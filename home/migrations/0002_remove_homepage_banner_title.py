# Generated by Django 4.0.3 on 2022-04-05 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_title',
        ),
    ]
