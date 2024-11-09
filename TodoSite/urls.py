
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("todoapp.urls"), name='todolist'),
    path('', include("aboutapp.urls"), name='home'),
    path('about/', include("aboutapp.urls"), name='about'),
    path('data/', include("aboutapp.urls"), name='std_data'),
    path('data/', include("aboutapp.urls"), name='teacher_data'),
   
]
