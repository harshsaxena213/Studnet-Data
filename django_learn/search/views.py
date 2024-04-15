from django.shortcuts import render
from django.http import request
from register.models import *

def search(request):
    # if request.method=="POST":
    #     data=request.POST 
    #     roll_number=data.get('roll_number')

    return render(request,"student_search.html")