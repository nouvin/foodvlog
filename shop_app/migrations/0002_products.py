# Generated by Django 2.2 on 2021-11-23 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='product')),
                ('stock', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('available', models.BooleanField()),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.categ')),
            ],
        ),
    ]
