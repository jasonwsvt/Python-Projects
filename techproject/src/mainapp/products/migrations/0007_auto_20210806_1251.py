# Generated by Django 2.1.5 on 2021-08-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210806_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('appetizers', 'appetizers'), ('drinks', 'drinks'), ('desserts', 'desserts')], max_length=60),
        ),
    ]
