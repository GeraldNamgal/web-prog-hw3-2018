# Generated by Django 2.0.4 on 2018-04-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='priceLarge',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='item',
            name='priceSmall',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='order',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=11),
        ),
    ]