# Generated by Django 2.1.5 on 2021-08-05 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20210805_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('----------', '----------'), ('Her Honour', 'Her Honour'), ('The Honourable', 'The Honourable'), ('Sire', 'Sire'), ('His Honour', 'His Honour'), ('The Right Honourable', 'The Right Honourable'), ('Dame', 'Dame'), ('Lord', 'Lord'), ('Doctor', 'Doctor'), ('Lady', 'Lady'), ('Excellency', 'Excellency'), ('Sir', 'Sir'), ('Esquire', 'Esquire')], default='----------', max_length=20),
        ),
    ]
