# Generated by Django 2.2 on 2021-04-21 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bdate',
            field=models.DateTimeField(null=True),
        ),
    ]
