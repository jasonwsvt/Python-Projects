# Generated by Django 2.2.5 on 2021-08-19 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BoardGames', '0003_auto_20210816_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boardgame',
            options={'ordering': ('-Favorite', 'Name', 'id')},
        ),
    ]
