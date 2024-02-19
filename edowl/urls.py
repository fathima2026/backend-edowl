
from django.contrib import admin
from django.urls import path,include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('users.urls')),
    path('api/',include('module.urls')),
    path('api-auth/',include('rest_framework.urls')),
    


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

