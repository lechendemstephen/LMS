from django.shortcuts import render
from .models import Course 
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