from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Teacher, Student

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return self.get_user(user.pk)

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return Teacher.objects.get(pk=user_id)
        except Teacher.DoesNotExist:
            try:
                return Student.objects.get(pk=user_id)
            except Student.DoesNotExist:
                return None