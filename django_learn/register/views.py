from django.shortcuts import render
from .models import *


def register(request):
    if request.method=="POST":
        data=request.POST
        pic=request.FILES.get("pic")
        name_student=data.get("name")
        father_name=data.get("father_name")
        address=data.get("address")
        stnd=data.get("stnd")
        email=data.get("email")
        number=data.get("number")
        roll=data.get("rollnumber")
        
        student_data.objects.create(
          name=name_student,
          stnd=stnd,
          address=address,
          number=number,
          father_name=father_name,
          email=email,
          pic=pic,
          roll=roll,
          )
        queryset=student_data.objects.all()

    return render(request,"register_student.html")

        