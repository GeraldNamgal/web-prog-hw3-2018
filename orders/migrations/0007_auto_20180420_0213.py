# Generated by Django 2.0.4 on 2018-04-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_customername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='orderNumber',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='orderNumber',
            field=models.IntegerField(default=1),
        ),
    ]
