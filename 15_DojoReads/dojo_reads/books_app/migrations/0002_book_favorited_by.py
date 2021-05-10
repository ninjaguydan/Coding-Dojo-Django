# Generated by Django 2.2 on 2021-05-08 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('books_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='login_app.User'),
        ),
    ]