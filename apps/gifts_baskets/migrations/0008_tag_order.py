# Generated by Django 5.0.4 on 2024-04-25 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts_baskets', '0007_alter_tag_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
