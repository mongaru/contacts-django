# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200, null=True)
    apodo = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

class Detalle(models.Model):
    contacto = models.ForeignKey('Contacto',blank=True, null=True)
    tipoDetalle = models.CharField(max_length=50)
    valorDetalle = models.CharField(max_length=100)

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    doc = models.IntegerField(unique=True,blank=True, null=True)
    picture = models.ImageField(upload_to = 'profile_images',null=True,blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=45, blank=True)
    avatar = models.ImageField(upload_to = 'pic_folder/', default = 'image/default.jpg')

    def __unicode__(self):
        return "%s - %s, %s" % (self.doc, self.user.first_name, self.user.last_name)
