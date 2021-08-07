# Generated by Django 2.1.5 on 2021-08-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20210805_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('Lady', 'Lady'), ('Sir', 'Sir'), ('Esquire', 'Esquire'), ('Excellency', 'Excellency'), ('Doctor', 'Doctor'), ('His Honour', 'His Honour'), ('Lord', 'Lord'), ('----------', '----------'), ('Her Honour', 'Her Honour'), ('Sire', 'Sire'), ('Dame', 'Dame'), ('The Honourable', 'The Honourable'), ('The Right Honourable', 'The Right Honourable')], default='----------', max_length=20),
        ),
    ]