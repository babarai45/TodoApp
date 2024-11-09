
#--------------`Function Based Views`-----------------#
# # Create your views here for function based views for simple return function values
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<h1>TodoApp page </h1>")




# --------------Function Based Views with Templates-----------------#
# it returns the template file from the templates folder of home.html
# 
# for we have to use render function from django.shortcuts
# syntax:
# render(request, 'template_name', context = {dictionary} , content_type = 'text/html', status = 200, using = None/jninja2 , template_name = None)
#
# render() function is used to render the template file from the templates folder
# request: HttpRequest object for the request
# template_name: name of the template file to render

# (other parameters are optional)

# context: dictionary to pass to the template file as context(contains the data to be displayed in the template)
# content_type: MIME type of the response content (default is 'text/html') MIME type is a standard that indicates the nature and format of a document
# status: status code for the response (defa
# from django.views.generic import TemplateView
# class HomePageView(TemplateView):
#     template_name = "home.html"ult is 200) status code is a standard response code indicating the success or failure of an HTTP request
# using: template engine to use for rendering the template file (default is None) Django uses its own template engine by default 
# template_name: name of the template file to render (default is None) if template_name is not provided, Django uses the name of the view function as the template name


# example:

# from django.shortcuts import render

# def home(request):
#     return render(request, 'todoapp/home.html', {'name': 'TodoApp'}, content_type='text/html', status=200, using=None, template_name=None)




# from django.shortcuts import render

# def home(request):
#     return render(request, 'todoapp/home.html')

    
# --------------    Class Based Views ------------------------#


# Class-based views are another way to define views in Django. They are used to handle requests and return responses.
# Class-based views are defined as classes that inherit from Django's generic views.
# Django provides several generic views that can be used to perform common tasks.
# Class-based views are more powerful and flexible than function-based views.


# when we use class based views we have to use class base url patterns in urls.py file

# from django.views import View
# from django.http import HttpResponse

# class HomeView(View):
#     def get(self, request):
#         return HttpResponse("<h1>Home Page</h1>")
    
#-----------------Function Based Views with Templates-----------------#

# function based url same for ruturning the templatle file or renturn function data
# function based views  with templates



# from django.views.generic import TemplateView

# class HomeView(TemplateView):
#     template_name = "todoapp/home.html"

    



# --------------    Asynchronous Views ------------------------#

# Asynchronous views are used to handle requests asynchronously. They are defined using the async and await keywords in Python.
# Asynchronous views are more efficient than synchronous views because they allow the server to handle multiple requests concurrently.


# from django.http import HttpResponse
# from django.shortcuts import render
# import asyncio


# async function returns the HttpResponse object with the content "<h1>Home Page</h1>"

# async def home(request):   
#     await asyncio.sleep(0)
#     return HttpResponse("<h1>Home Page</h1>")



# async function returns the template file from the templates folder of home.html
# async def home(request):
#     await asyncio.sleep(0)
#     return render(request, 'todoapp/home.html')




# --------------    Class Based Views with async ------------------------#

from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
import asyncio

# class HomeView(View):
#     async def get(self, request):
#         await asyncio.sleep(0)
#         return HttpResponse("<h1>Home Page</h1>")
    
class HomeView(View):
    async def get(self, request):
        await asyncio.sleep(0)
        return render(request, 'todoapp/home.html')
    


# best practice is to use class based views with async function
