from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    mobile_no = models.IntegerField()
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.mobile_no} {self.joined_date}"

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    standard = models.IntegerField()
    Rollno = models.IntegerField()
    created_by= models.CharField(max_length=30)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.Rollno} {self.created_by}"





