# Generated by Django 2.1.5 on 2021-08-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210805_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('drinks', 'drinks'), ('appetizers', 'appetizers'), ('desserts', 'desserts')], max_length=60),
        ),
    ]