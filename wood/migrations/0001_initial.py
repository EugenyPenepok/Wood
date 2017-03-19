# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('skype', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('postcode', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Coating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='ConcreteProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('number', models.IntegerField()),
                ('time_production', models.DateTimeField()),
                ('coating', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.Coating')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=1000)),
                ('concrete_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.ConcreteProduct')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=13)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=300)),
                ('information', models.CharField(max_length=5000)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.Client')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('requirements', models.CharField(max_length=5000)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.Client')),
            ],
        ),
        migrations.CreateModel(
            name='PositionInOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('concrete_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.ConcreteProduct')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfDelivery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='type_of_delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.TypeOfDelivery'),
        ),
        migrations.AddField(
            model_name='concreteproduct',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.Material'),
        ),
        migrations.AddField(
            model_name='concreteproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.Product'),
        ),
        migrations.AddField(
            model_name='concreteproduct',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.Size'),
        ),
    ]
