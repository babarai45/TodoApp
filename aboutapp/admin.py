from django.contrib import admin

# Register your models here.

from .models import Std_Data , Teacher_Data


# here we have to register the model class in admin panel 

# admin.site.register(Std_Data)
# admin.site.register(Teacher_Data)



#-----------------to show the multiple field data in admin panel----------------

# class Std_DataAdmin(admin.ModelAdmin):
#     list_display = ['fname', 'lname', 'email', 'phone', 'address', 'city', 'state', 'course', 'fee']

# admin.site.register(Std_Data, Std_DataAdmin)

# class Teacher_DataAdmin(admin.ModelAdmin):
#     list_display = ['fname', 'lname', 'email', 'phone', 'address', 'city', 'state', 'subject', 'salary', 'experience', 'qualification']

# admin.site.register(Teacher_Data, Teacher_DataAdmin)


# using decorator best practice
@admin.register(Std_Data)
class Std_DataAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'phone', 'address', 'city', 'state', 'course', 'fee']


@admin.register(Teacher_Data)
class Teacher_DataAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'phone', 'address', 'city', 'state', 'subject', 'salary', 'experience', 'qualification']