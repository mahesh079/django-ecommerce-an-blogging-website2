# Generated by Django 3.0.6 on 2020-09-22 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_orders_items_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]