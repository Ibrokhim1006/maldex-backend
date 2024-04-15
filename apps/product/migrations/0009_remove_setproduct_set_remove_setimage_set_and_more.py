# Generated by Django 5.0.2 on 2024-04-15 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_merge_20240415_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setproduct',
            name='set',
        ),
        migrations.RemoveField(
            model_name='setimage',
            name='set',
        ),
        migrations.RemoveField(
            model_name='setproduct',
            name='product',
        ),
        migrations.AlterModelOptions(
            name='productcategories',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категория'},
        ),
        migrations.DeleteModel(
            name='Set',
        ),
        migrations.DeleteModel(
            name='SetImage',
        ),
        migrations.DeleteModel(
            name='SetProduct',
        ),
    ]