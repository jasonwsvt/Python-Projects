# Generated by Django 2.2.5 on 2021-08-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoardGames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgame',
            name='Image',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='Thumbnail',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]