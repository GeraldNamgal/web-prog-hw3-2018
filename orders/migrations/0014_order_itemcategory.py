# Generated by Django 2.0.4 on 2018-04-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20180415_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='itemCategory',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
