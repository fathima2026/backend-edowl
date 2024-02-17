from django.db import models
from users.models import Teacher, Student

class Module(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    tasks = models.DecimalField(decimal_places=1,max_digits=5,default=0,blank=True,null=True)
    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=255)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class StudentCourseEnrollment(models.Model):
    course = models.ForeignKey(Module, on_delete=models.CASCADE,related_name='enrolled_courses')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrolled_students')    
    enrolled_time = models.TimeField(auto_now=True)
    enrolled_date = models.DateField(auto_now=True)


    class Meta:
        verbose_name_plural = "6. Enrolled courses"

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=None,default='')
    file = models.FileField(upload_to='files/',null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    total_mark = models.IntegerField(default=50)
    module = models.ForeignKey(Module, on_delete=models.CASCADE,related_name='assignment')
    created_time = models.TimeField(auto_now=True)
    created_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "7. Assignments"

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE,related_name='submitted_assignments')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(blank=True,null=True)
    completed_time = models.TimeField(auto_now=True)
    completed_date = models.DateField(auto_now=True)
    marks = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    remarks = models.CharField(max_length=None,null=True,blank=True)
    
    class Meta :
        verbose_name = "8. Submitted assignments"

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    quiz = models.JSONField(blank=True,null=True)
    file = models.FileField(blank=True,null=True)
    module=models.ForeignKey(Module, on_delete=models.CASCADE,related_name='quiz')
    total_mark = models.IntegerField(default=50)
    created_time = models.TimeField(auto_now=True)
    created_date = models.DateField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    duration = models.IntegerField(default="0")

    class Meta :
       verbose_name = "8. quiz"

class QuizSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='submitted_quiz')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(blank=True,null=True)
    marks = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    remarks = models.CharField(max_length=None,null=True,blank=True)
    completed_time = models.TimeField(auto_now=True)
    completed_date = models.DateField(auto_now=True)

    class Meta :
       verbose_name = "8. Submitted Quiz"

class Hangman(models.Model):
    title = models.CharField(max_length=255)
    module=models.ForeignKey(Module, on_delete=models.CASCADE,related_name='hangman')
    words = models.JSONField(blank=True,null=True)
    hints = models.JSONField(blank=True,null=True)
    total_mark = models.IntegerField(default=50)
    created_time = models.TimeField(auto_now=True)
    created_date = models.DateField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)

    class Meta :
       verbose_name = "9. hangman"

class HangmanSubmission(models.Model):
    hangman = models.ForeignKey(Hangman, on_delete=models.CASCADE, related_name='submitted_hangman')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    completed_time = models.TimeField(auto_now=True)
    completed_date = models.DateField(auto_now=True)

    class Meta :
       verbose_name = "10. Submitted hangman"


