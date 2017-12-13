# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cars(models.Model):
    marka = models.CharField(max_length=120)
    segment = models.TextField()
    cikistarihi = models.DateTimeField()

class Motorcycle(models.Model):
    marka = models.CharField(max_length=120)
    segment = models.TextField()
    cikistarihi = models.DateTimeField()