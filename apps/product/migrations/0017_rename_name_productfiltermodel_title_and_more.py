# Generated by Django 5.0.4 on 2024-05-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_productfilterproducts_filter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productfiltermodel',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.CharField(blank=True, max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='Уникальный идентификатор'),
        ),
    ]
