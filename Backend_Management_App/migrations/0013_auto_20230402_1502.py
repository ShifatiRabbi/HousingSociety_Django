# Generated by Django 3.2.5 on 2023-04-02 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend_Management_App', '0012_auto_20230402_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centeravailability',
            name='type',
            field=models.IntegerField(choices=[(0, 'Available'), (1, 'Booked')], default=0),
        ),
        migrations.AlterField(
            model_name='groundavailability',
            name='type',
            field=models.IntegerField(choices=[(0, 'Available'), (1, 'Booked')], default=0),
        ),
    ]