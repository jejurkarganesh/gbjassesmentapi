from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

swagger_view = get_swagger_view(title='ASESSMENT TEST API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth', views.ObtainAuthToken.as_view()),
    path('accounts/', include('accounts.urls')),
    path('quiz/', include('questions.urls')),
    url(r'swagger/', swagger_view),
]
