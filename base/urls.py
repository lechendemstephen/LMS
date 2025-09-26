from django.urls import path 
from . import views

urlpatterns = [
    path('', views.courses, name='courses'), 
    path('courses/<course_slug>', views.course_detail, name='course_detail'),


    # authentication urls 

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout, name='logout'),




    # dashboard 

    path('dashboard/', views.dashboard, name="dashboard")

]
