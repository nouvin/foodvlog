# Generated by Django 2.2 on 2021-11-23 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_auto_20211123_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='catagory',
            new_name='category',
        ),
    ]
