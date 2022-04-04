# Generated by Django 4.0.3 on 2022-04-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, help_text='A slug to identify post by category', max_length=255, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Blog Category',
                'verbose_name_plural': 'Blog Categories',
                'ordering': ('name',),
            },
        ),
    ]
