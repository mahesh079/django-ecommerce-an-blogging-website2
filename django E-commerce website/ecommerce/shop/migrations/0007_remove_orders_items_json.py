# Generated by Django 3.0.6 on 2020-09-22 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='items_json',
        ),
    ]
