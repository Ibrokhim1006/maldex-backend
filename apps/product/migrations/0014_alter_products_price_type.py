# Generated by Django 5.0.2 on 2024-04-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_productcategories_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price_type',
            field=models.CharField(choices=[('RUB', 'RUB'), ('USD', 'USD')], default='RUB', max_length=10, verbose_name='Цена валюта'),
        ),
    ]
