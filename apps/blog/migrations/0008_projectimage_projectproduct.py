# Generated by Django 5.0.4 on 2024-04-24 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_tag_object_id'),
        ('product', '0003_productcategories_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects/', verbose_name='image')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='blog.project')),
            ],
        ),
    ]
