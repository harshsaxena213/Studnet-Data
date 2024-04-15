from django.db import models

class student_data(models.Model):
    pic=models.ImageField(null=False)
    name=models.TextField(null=False)
    father_name=models.TextField(null=False)
    stnd=models.IntegerField(null=False)
    address=models.TextField(null=False)
    email=models.EmailField(null=True)
    number=models.TextField(null=False)
    roll=models.IntegerField(null=False)
    