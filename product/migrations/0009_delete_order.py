# Generated by Django 4.2.4 on 2023-09-24 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_order_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
