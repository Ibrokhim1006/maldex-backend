import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_sitelogo_alter_productcategories_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='colorID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.colors', verbose_name='Цвета'),
            preserve_default=False,
        ),
    ]