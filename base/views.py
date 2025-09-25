from django.shortcuts import render
from .models import Course 
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.


def courses(request): 
    all_courses = Course.objects.all() 


    context = {
        "courses": all_courses
    }

    return render(request, 'courses/courses.html', context)



def course_detail(request, course_id): 

    single_course = Course.objects.filter(id=course_id).first()
     
    context = {
        'single_course': single_course
    }

    return render(request, 'courses/course_detail.html', context)


# authentication 

def register(request):


    return render(request, 'registration/signup.html')



def login_view(request):


    return render(request, 'registration/login.html')

def logout_view(request):

    logout(request)

    messages.info(request, "you have successfully logged out")

    return redirect('login/')