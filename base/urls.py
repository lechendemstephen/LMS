from django.urls import path 
from . import views

urlpatterns = [
    path('courses/', views.courses, name='courses'), 
    path('courses/<course_id>', views.course_detail, name='course_detail'),


    # authentication urls 

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),

]
