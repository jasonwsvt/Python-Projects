# Generated by Django 2.2.5 on 2021-08-17 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoardGames', '0002_auto_20210814_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boardgame',
            options={'ordering': ('-Favorite',)},
        ),
        migrations.AddField(
            model_name='boardgame',
            name='Favorite',
            field=models.BooleanField(default=False),
        ),
    ]
