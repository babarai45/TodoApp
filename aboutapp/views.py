from django.shortcuts import render
from django.views.generic import TemplateView
import asyncio
# Create your views here.



# class AboutView(TemplateView):
#     async def get(self, request):   # get method is used to handle the get request
#         await asyncio.sleep(0)
#         return render(request, 'aboutapp/about.html')




# from django.views.generic.base import TemplateView

class AboutView(TemplateView):
    template_name = 'aboutapp/base.html'

    async def hoem_get(self, request):  # here you can use any name instead of get like about_get
        await asyncio.sleep(0)
        return render(request, self.template_name)


class AboutView(TemplateView):
    template_name = 'aboutapp/about.html'

    async def about_get(self, request):  # here you can use any name instead of get like about_get
        await asyncio.sleep(0)
        return render(request, self.template_name)



#-------------i want show db data i on front end----------------
# import your model class

from .models import Std_Data , Teacher_Data


# def StudentData(request):
#     std_data = Std_Data.objects.all()
#     print("your data is", std_data) # it will print the data in console
#     return render(request, 'aboutapp/std_data.html', {'std': std_data})


# calass based view

from django.views.generic import TemplateView
from django.shortcuts import render
class StudentData(TemplateView):
    template_name = 'aboutapp/std_data.html'

    def get(self, request):
        std_data = Std_Data.objects.all()
        return render(request, self.template_name, {'std': std_data})
    

# add data in student by user input on front end

from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Std_Data

class AddStudentData(TemplateView):
    template_name = 'aboutapp/add_std_data.html'

    def post(self, request):
        if request.method == 'POST':
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            course = request.POST.get('course')
            fee = request.POST.get('fee')

            std_data = Std_Data(fname=fname, lname=lname, email=email, phone=phone, address=address, city=city, state=state, course=course, fee=fee)
            std_data.save()
            return render(request, self.template_name)
        return render(request, self.template_name)
    
    

class TeacherData(TemplateView):
    template_name = 'aboutapp/td.html'

    def get(self, request):
        teah_data = Teacher_Data.objects.all()
        return render(request, self.template_name, {'td': teah_data})