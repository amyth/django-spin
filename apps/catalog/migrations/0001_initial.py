# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 07:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('level', models.IntegerField(default=0)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=30, verbose_name='SKU')),
                ('title', models.CharField(max_length=140, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.BigIntegerField(verbose_name='price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('property_type', models.IntegerField(choices=[(0, b'Single Value')], default=0, verbose_name='property type')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='catalog.Product')),
            ],
            options={
                'verbose_name_plural': 'Product Properties',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='name')),
                ('price', models.BigIntegerField(verbose_name='price')),
                ('deliveries', models.IntegerField()),
                ('valid_for_days', models.IntegerField(default=7)),
                ('products', models.ManyToManyField(related_name='subscriptions', to='catalog.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.BigIntegerField(blank=True, null=True, verbose_name='price')),
                ('quantity', models.BigIntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='catalog.Product')),
                ('stores', models.ManyToManyField(to='home.Store')),
            ],
        ),
        migrations.CreateModel(
            name='VariantImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'media/images/products/')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Variant')),
            ],
        ),
        migrations.CreateModel(
            name='VariantProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='value')),
                ('product_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.ProductProperty')),
            ],
        ),
    ]
