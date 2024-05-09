# Generated by Django 5.0.4 on 2024-05-09 13:34

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Уникальный идентификатор')),
                ('name', models.CharField(max_length=155, verbose_name='Название баннера')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('order_by_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='Order By ID')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннер',
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='BannerCarousel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Уникальный идентификатор')),
                ('name', models.CharField(blank=True, max_length=155, null=True, verbose_name='Название баннерной карусели')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Баннер-карусель',
                'verbose_name_plural': 'Баннер-карусель',
                'db_table': 'banner_carousel',
            },
        ),
        migrations.CreateModel(
            name='BannerCarouselProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Уникальный идентификатор')),
                ('bannerCarouselVideo', models.FileField(blank=True, null=True, upload_to='media/banner/carousel/video/', verbose_name='Баннер-карусель Видео')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('bannerCarouselID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bannerCarouselID', to='banner.bannercarousel', verbose_name='Идентификатор баннерной карусели')),
                ('productCarouselID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bannerCarouselProduct', to='product.products', verbose_name='Идентификатор карусели товаров баннера')),
            ],
            options={
                'verbose_name': 'Баннер-карусель Продукт',
                'verbose_name_plural': 'Баннер-карусель Продукт',
                'db_table': 'banner_carousel_product',
            },
        ),
        migrations.CreateModel(
            name='BannerProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Уникальный идентификатор')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('bannerID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bannerID', to='banner.banner', verbose_name='Идентификатор баннера')),
                ('productID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bannerProduct', to='product.products', verbose_name='Идентификатор товара')),
            ],
            options={
                'verbose_name': 'Продукт Баннера',
                'verbose_name_plural': 'Продукт Баннера',
                'db_table': 'banner_product',
            },
        ),
    ]
