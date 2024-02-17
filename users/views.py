from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import generics
from .serializers import TeacherSerializer, StudentSerializer, YourCustomTokenObtainPairSerializer
from . import models
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status

User = get_user_model()

class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

class CustomDjoserUserViewSet(DjoserUserViewSet):
    queryset = User.objects.all()

# Your login views can be removed as djoser handles login and registration.

@api_view(['POST'])
@permission_classes([AllowAny])
def student_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    student = authenticate(email=email, password=password)

    if student is not None:
        serializer = YourCustomTokenObtainPairSerializer(data={'email': email, 'password': password})
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data
        return Response({
            'bool': True,
            'is_student': student.is_student,
            'is_staff': student.is_staff,
            'id': student.id,
            'access': str(tokens['access']),
            'refresh': str(tokens['refresh']),
            'first_name': student.first_name
        })
    else:
        return Response({'bool': False, 'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def teacher_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    teacher = authenticate(email=email, password=password)

    if teacher is not None:
        serializer = YourCustomTokenObtainPairSerializer(data={'email': email, 'password': password})
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data
        return Response({
            'bool': True,
            'is_staff': teacher.is_staff,
            'is_teacher': teacher.is_teacher,
            'id': teacher.id,
            'access': str(tokens['access']),
            'refresh': str(tokens['refresh']),
            'first_name': teacher.first_name
        })
    else:
        return Response({'bool': False, 'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
# @csrf_exempt
# def student_login(request):
#    email = request.POST['email']
#    password = request.POST['password']
#    try:
#       studentData = models.Student.objects.get(email=email, password=password)
#    except models.Student.DoesNotExist:
#       studentData=None
#    if studentData:
#       return JsonResponse({'bool':True,'is_student':studentData.is_student,'is_teacher':studentData.is_teacher,'is_staff':studentData.is_staff, 'id':studentData.id})
#    else:
#       return JsonResponse({'bool':False})
   
# @csrf_exempt
# def teacher_login(request):
#    email = request.POST['email']
#    password = request.POST['password']
#    try:
#       teacherData = models.Teacher.objects.get(email=email, password=password)
#    except models.Teacher.DoesNotExist:
#       teacherData=None
#    if teacherData:
#       return JsonResponse({'bool':True,'is_student':teacherData.is_student,'is_teacher':teacherData.is_teacher,'is_staff':teacherData.is_staff, 'id':teacherData.id})
#    else:
#       return JsonResponse({'bool':False})
   

