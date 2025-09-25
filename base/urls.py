from django.urls import path 
from . import views

urlpatterns = [
    path('courses/', views.courses, name='courses'), 
    path('courses/<course_id>', views.course_detail, name='course_detail'),


    # authentication urls 

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout, name='logout')

]
