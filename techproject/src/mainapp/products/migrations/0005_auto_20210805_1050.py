# Generated by Django 2.1.5 on 2021-08-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210805_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('entrees', 'entrees'), ('desserts', 'desserts'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
