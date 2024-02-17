from django.contrib import admin
from . import models
# Register your models here.
admin. site. register(models.Module)
admin. site. register(models.StudentCourseEnrollment)
admin. site. register(models.Assignment)
admin. site. register(models.AssignmentSubmission)
admin. site. register(models.Quiz)
admin. site. register(models.QuizSubmission)
admin. site. register(models.Hangman)
admin. site. register(models.HangmanSubmission)