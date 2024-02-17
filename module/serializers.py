from rest_framework import serializers
from . import models
from users.models import Student


class ModuleSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Module
        fields = ['id','title', 'description', 'teacher','code','tasks']

class TopicSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Topic
        fields = ['id','title', 'module']

class EnrolledModuleSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.StudentCourseEnrollment
        fields = ['id','course','student','enrolled_time','enrolled_date']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Assignment
        fields = ['id','title','description','file','image','total_mark','module','created_time','created_date']

class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.AssignmentSubmission
        fields = ['id','assignment','student','file','completed_time','completed_date','marks','remarks']

# class AssignmentAccessSerializer(serializers.ModelSerializer):
#     class Meta :
#         model = models.AssignmentSubmission
#         fields = ['id','assignment','student','file','completed_time','completed_date','marks','remarks','is_graded']
#         depth=1

class AssignmentAccessSerializer(serializers.ModelSerializer):
    is_graded = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.AssignmentSubmission
        fields = ['id', 'assignment', 'student', 'file', 'completed_time', 'completed_date', 'marks', 'remarks', 'is_graded']
        depth=1
    def get_is_graded(self, obj):
        return obj.marks is not None
    
class QuizSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Quiz
        fields = ['id','title','quiz','module','total_mark','created_time','created_date','due_date','duration','file']


class QuizSubmissionSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.QuizSubmission
        fields = ['id','quiz','student','marks','remarks','file','completed_time','completed_date']


class HangmanSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Hangman
        fields = ['id','title','module','words','hints','total_mark','created_time','created_date','due_date']


class HangmanSubmissionSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.HangmanSubmission
        fields = ['id','hangman','student','marks','completed_time','completed_date']

class HangmanAccessSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.HangmanSubmission
        fields = ['id','hangman','student','marks','completed_time','completed_date']
        depth=1
        
