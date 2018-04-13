# Generated by Django 2.0.4 on 2018-04-10 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('priceSmall', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('priceLarge', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='DinnerPlatter',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='orders.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='orders.Item')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaRegular',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='orders.Item')),
                ('toppings', models.ManyToManyField(blank=True, to='orders.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaSicilian',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='orders.Item')),
                ('toppings', models.ManyToManyField(blank=True, to='orders.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='orders.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='orders.Item')),
                ('xtraCheese', models.BooleanField(default=False)),
                ('mushrooms', models.BooleanField(default=False)),
                ('greenPeppers', models.BooleanField(default=False)),
                ('onions', models.BooleanField(default=False)),
            ],
        ),
    ]
