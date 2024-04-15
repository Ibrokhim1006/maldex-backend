# Generated by Django 5.0.2 on 2024-04-15 06:50

import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('type', models.CharField(choices=[('home', 'home'), ('other', 'other')], max_length=10)),
                ('order', models.PositiveSmallIntegerField(blank=True, unique=True)),
            ],
        ),
    ]