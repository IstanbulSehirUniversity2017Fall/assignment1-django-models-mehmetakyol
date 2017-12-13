# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Cars
from .models import Motorcycle

admin.site.register(Cars)
admin.site.register(Motorcycle)

from django.contrib import admin

# Register your models here.
