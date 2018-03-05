# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from customer.models import Product
# Create your views here.

#def index(request,name):
   #return HttpResponse("Hello  "+name+"  hahaha")
 #  return render(request,"index.html",{})

def index(request):
    if request.POST:
        post_data=request.POST
        name=post_data.get("name","")
        description=post_data.get("description","")
        enabled=post_data.get("enabled","").lower()
        price=post_data.get("price","")
        
        if enabled == "true":
        	enabled=True
        else:
        	 enabled =False

        product=Product(
        	name = name,
        	description = description,
        	enabled = enabled,
        	price = float(price),
        	)
        product.save()
        return redirect("/prodlist/")
    return render(request,"index.html",{})


def prodlist(request):


    products = Product.objects.all()
    return render(request,"list.html",{"products":products})
