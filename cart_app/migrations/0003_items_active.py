# Generated by Django 2.2 on 2021-11-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0002_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
