# Generated by Django 5.0.2 on 2024-03-13 13:41

import ckeditor.fields
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_products_dimensions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colors',
            options={'verbose_name': 'Цвет', 'verbose_name_plural': 'Цвет'},
        ),
        migrations.AlterModelOptions(
            name='productcategories',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категория'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Изображения продукта', 'verbose_name_plural': 'Изображения продукта'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукт'},
        ),
        migrations.RemoveField(
            model_name='products',
            name='height',
        ),
        migrations.RemoveField(
            model_name='products',
            name='length',
        ),
        migrations.RemoveField(
            model_name='products',
            name='width',
        ),
        migrations.AddField(
            model_name='products',
            name='gross_weight',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Вес брутто'),
        ),
        migrations.AddField(
            model_name='products',
            name='package_dimensions',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Размеры упаковки'),
        ),
        migrations.AddField(
            model_name='products',
            name='package_quantity',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Количество упаковки'),
        ),
        migrations.AddField(
            model_name='products',
            name='package_wight',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Вес упаковки'),
        ),
        migrations.AlterField(
            model_name='colors',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='colors', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='colors',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название цвета'),
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='media/category/icon/', verbose_name='Категория значка'),
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Уникальный идентификатор'),
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='is_hit',
            field=models.BooleanField(default=False, verbose_name='Хит?'),
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='Новый?'),
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='is_popular',
            field=models.BooleanField(default=False, verbose_name='Популярен?'),
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='media/category/logo/', verbose_name='Категория логотипа'),
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colorProduct', to='product.colors', verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='product/images', verbose_name='Изображений'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='productID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productID', to='product.products', verbose_name='Код товара'),
        ),
        migrations.AlterField(
            model_name='products',
            name='brand',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='products',
            name='categoryId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProductSubCategoryID', to='product.productcategories', verbose_name='Категория продукта'),
        ),
        migrations.AlterField(
            model_name='products',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Описания'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Данные опубликованы'),
        ),
        migrations.AlterField(
            model_name='products',
            name='dimensions',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Размеры'),
        ),
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Уникальный идентификатор'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='main-image', verbose_name='Главное фото'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_hit',
            field=models.BooleanField(default=False, verbose_name='Хит?'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='Новый?'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_popular',
            field=models.BooleanField(default=False, verbose_name='Популярен?'),
        ),
        migrations.AlterField(
            model_name='products',
            name='material',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Название продукта'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price_type',
            field=models.CharField(blank=True, choices=[('RUB', 'Rub'), ('USD', 'Usd')], default='RUB', max_length=10, null=True, verbose_name='Цена валюта'),
        ),
    ]
