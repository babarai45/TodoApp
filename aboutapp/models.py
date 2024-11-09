from django.db import models

# Create your models here.


# stuednt data model
class Std_Data(models.Model):

    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    course = models.CharField(max_length=100,default='B.Tech')
    fee = models.IntegerField(default=10000)

# Teacher data model
class Teacher_Data(models.Model):

    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    salary = models.IntegerField()
    experience = models.IntegerField()
    qualification = models.CharField(max_length=100)


# return the data in string format
    # def __str__(self):
    #     return self.fname

# but problem is that we are not able to see the data in admin panel
# becaues it return only one field data in admin panel so we have to return the multiple field data in admin panel



# so we have to use list_display in admin.py file to show the multiple field data in admin panel