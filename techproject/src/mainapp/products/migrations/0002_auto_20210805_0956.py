# Generated by Django 2.1.5 on 2021-08-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('appetizers', 'appetizers'), ('desserts', 'desserts'), ('drinks', 'drinks')], max_length=60),
        ),
    ]