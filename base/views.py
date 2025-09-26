from django.shortcuts import render
from .models import Course, Enrollment
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

# Create your views here.


def courses(request): 
    all_courses = Course.objects.all() 


    context = {
        "courses": all_courses
    }

    return render(request, 'courses/courses.html', context)



def course_detail(request, course_slug): 

    # single_course = Course.objects.filter().first()
     
    context = {
        'single_course': "ok"
    }

    return render(request, 'courses/course_detail.html', context)

def enroll_courses(request, course_id): 
    single_course = Course.objects.filter(id=course_id)

    enrolled_course = Enrollment.objects.create(
        student = request.user, 
    )

    return redirect('')

# authentication 

def register(request):


    return render(request, 'registration/signup.html')



def login_view(request):

    if request.user.is_authenticated: 
        return redirect(getattr(settings, "LOGIN_REDIRECT_URL", "/"))


    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid(): 
        user = form.get_user()

        login(request, user)

        if not request.POST.get("remember"): 
            request.session.set_expiry(0)
        messages.success(request, "Signed in successfully")
        next_url = request.POST.get("next") or request.GET.get("next") or getattr(settings, "LOGIN_REDIRECT_URL", "/")

        return redirect(next_url)
        

    return render(request, 'registration/login.html', {
        "form": form 
    })

def logout_view(request):

    logout(request)

    messages.info(request, "you have successfully logged out")

    return redirect('')


# dasboard 
@login_required
def dashboard(request): 


    return render(request, 'courses/dashboard.html')