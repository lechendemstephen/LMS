from django.db import models
from django.conf import settings 

User = settings.AUTH_USER_MODEL 

# Create your models here.

class Student(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    bio = models.TextField(blank=True) 
    enrolled_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 

        return self.user.username 
    

class Course(models.Model): 
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"

    LEVEL = [
        (BEGINNER, "BEGINNER"),
        (INTERMEDIATE, "INTERMEDIATE"),
        (ADVANCED, "ADVANCED"),
    ]

    title = models.CharField(blank=True, max_length=50)
    slug = models.SlugField(blank=True, max_length=500)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='courses', blank=True)
    level = models.CharField(max_length=20, choices=LEVEL, default=BEGINNER)
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses_taught")

    def __str__(self): 

        return self.title

class Enrollment(models.Model): 
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        unique_together = ("student", "course")

    
    def __str__(self): 

        return self.student
    


