# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-20 14:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('apodo', models.CharField(max_length=100, null=True)),
                ('telefono', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDetalle', models.CharField(max_length=50)),
                ('valorDetalle', models.CharField(max_length=100)),
                ('contacto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Contacto')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('doc', models.IntegerField(blank=True, null=True, unique=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('telefono', models.CharField(blank=True, max_length=15)),
                ('direccion', models.CharField(blank=True, max_length=45)),
                ('avatar', models.ImageField(default='image/default.jpg', upload_to='pic_folder/')),
            ],
        ),
    ]
