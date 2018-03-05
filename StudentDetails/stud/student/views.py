# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from student.models import Student
# Create your views here.
def add(request):
    if request.POST:
        post_data=request.POST
        name=post_data.get("name","")
        rollno=post_data.get("rollno","")
        Class=post_data.get("Class","")
        gender=post_data.get("gender","")
        address=post_data.get("address","")

        stud=Student(
          name=name,
          rollno=rollno,
          Class=Class,
          gender=gender,
          address=address,
          )
        stud.save()
        return redirect("/studlist/")
    return render(request,"form.html",{})

def studlist(request):

   stud=Student.objects.all()
   return render(request,"studlist.html",{"stud":stud})   

   

