# Generated by Django 4.1.7 on 2023-03-16 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_menuitems'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='confirmedbooking',
            options={'verbose_name': 'Confirmed Booking', 'verbose_name_plural': 'Confirmed Bookings'},
        ),
        migrations.AlterModelOptions(
            name='menuitems',
            options={'verbose_name': 'Menu Item', 'verbose_name_plural': 'Menu Items'},
        ),
    ]
