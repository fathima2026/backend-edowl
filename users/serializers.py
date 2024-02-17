from rest_framework import serializers

from .models import Teacher, Student, BaseUser
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers

class YourCustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data
    
from rest_framework import serializers
from .models import Teacher, Student

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser  # Replace with your actual base user model
        fields = ['id', 'email', 'first_name', 'last_name', 'password']

class TeacherSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = Teacher
        fields = BaseUserSerializer.Meta.fields + ['is_teacher']  # Add teacher-specific fields

    def create(self, validated_data):
        # Ensure the password is hashed before saving
        password = validated_data.pop('password', None)
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance

class StudentSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = Student
        fields = BaseUserSerializer.Meta.fields + ['is_student']  # Add student-specific fields

    def create(self, validated_data):
        # Ensure the password is hashed before saving
        password = validated_data.pop('password', None)
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance

