# Generated by Django 2.2 on 2021-11-25 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0003_items_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='quantity',
            new_name='quan',
        ),
    ]
