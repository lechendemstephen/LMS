from django.contrib import admin
from .models import Student, Course, Enrollment
# Register your models here.


class StudentAdmin(admin.ModelAdmin): 
    list_display = (
        "user", "bio", "enrolled_date"
    )


class EnrolledAdmin(admin.ModelAdmin): 
    list_display = (
        "student", "course", "enrolled_at"
    )
    

class CourseAdmin(admin.ModelAdmin): 
    list_display = (
        "title", "description", "level", "created_at", "instructor"
    )
    


admin.site.register(Student, StudentAdmin)
admin.site.register(Enrollment, EnrolledAdmin)
admin.site.register(Course, CourseAdmin)
