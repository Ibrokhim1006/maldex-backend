# Generated by Django 5.0.4 on 2024-05-11 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_productfilterproducts_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('-updated_at',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукт'},
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Данные опубликованы'),
        ),
        migrations.AlterField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
