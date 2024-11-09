
# todoapp/urls.py


#-----------------Function Based Views with Templates-----------------#

# function based url same for ruturning the templatle file or renturn function data
# function based views  with templates


# from django.urls import path

# from . import views

# urlpatterns = [
    
#         path('blog/', views.home, name='home'),
#     ]





# --------------    Class Based Views ------------------------#


# class based views with templates

# little bit change in urls.py file for class based views
# in which we add "as_view()" method in the views.py file
# as_view() method is used to convert the class based views into function based views

from django.urls import path
from .views import HomeView

urlpatterns = [
    path('blog/', HomeView.as_view()),
]