# Generated by Django 5.0.4 on 2024-05-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_productcategories_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='prints',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
