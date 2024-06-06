# Generated by Django 5.0.4 on 2024-06-06 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_sitelogo_alter_productcategories_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='colorID',
            field=models.ForeignKey(default='fbf0fc9a-c116-44d3-a285-6b6f257f8c57', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.colors', verbose_name='Цвета'),
            preserve_default=False,
        ),
    ]
