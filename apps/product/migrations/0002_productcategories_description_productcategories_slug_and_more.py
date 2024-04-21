# Generated by Django 5.0.4 on 2024-04-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategories',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcategories',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productcategories',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Уникальный идентификатор'),
        ),
    ]
