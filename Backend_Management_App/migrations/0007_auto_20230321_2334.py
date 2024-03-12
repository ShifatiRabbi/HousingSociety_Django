# Generated by Django 3.2.5 on 2023-03-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend_Management_App', '0006_auto_20230321_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[('available', 'Available'), ('pending', 'Pending'), ('booked', 'Booked')], max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='payment_status',
            field=models.CharField(choices=[('full', 'Full PAID'), ('minimum', 'Minimum PAID'), ('not_paid', 'Not PAID')], max_length=20),
        ),
    ]