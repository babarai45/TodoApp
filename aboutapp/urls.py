from django.urls import path

from . import views

urlpatterns = [
    path('', views.AboutView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('std/', views.StudentData.as_view(), name='std_data'),
    # path('data/', views.StudentData, name='std_data'),
    path('td/', views.TeacherData.as_view(), name='teacher_data'),
]
 