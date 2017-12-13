# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from .models import Cars

# Create your views here.

def home_view(request,marka):
    item_cars = Cars.objects.all()



    A=0
    for i in item_cars:
        if (A > 1):
            break

        if(i.marka == "BMW"):
            A=A+1

            return HttpResponse('<h>%s comforline</h>' %i.marka)

        if(i.marka =="Audi"):
            return HttpResponse('<h>%s comfort</h>' % i.marka)





    #return HttpResponse('<h>hosgeldin</h>')