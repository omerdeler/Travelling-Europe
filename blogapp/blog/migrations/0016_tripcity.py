# Generated by Django 3.2.9 on 2023-05-05 13:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_blogcity_category_ulke'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='Ulkeler')),
                ('description', ckeditor.fields.RichTextField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_home', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False, null=True, unique=True)),
            ],
        ),
    ]