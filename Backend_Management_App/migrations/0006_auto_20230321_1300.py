# Generated by Django 3.2.5 on 2023-03-21 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend_Management_App', '0005_booking_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[(1, 'Available'), (2, 'Pending'), (3, 'Booked')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='payment_status',
            field=models.CharField(choices=[(1, 'Full PAID'), (2, 'Mnimum PAID'), (3, 'Not PAIID')], max_length=20),
        ),
    ]