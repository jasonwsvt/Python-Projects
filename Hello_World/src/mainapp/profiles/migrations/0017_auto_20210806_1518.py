# Generated by Django 2.1.5 on 2021-08-06 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20210806_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('Lord', 'Lord'), ('The Right Honourable', 'The Right Honourable'), ('Excellency', 'Excellency'), ('Dame', 'Dame'), ('Lady', 'Lady'), ('----------', '----------'), ('His Honour', 'His Honour'), ('Sire', 'Sire'), ('Doctor', 'Doctor'), ('Her Honour', 'Her Honour'), ('Esquire', 'Esquire'), ('Sir', 'Sir'), ('The Honourable', 'The Honourable')], default='----------', max_length=20),
        ),
    ]
