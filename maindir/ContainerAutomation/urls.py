
from django.contrib import admin
from django.urls import path, include
from k8s_container_automation import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('k8s_container_automation.urls')),
]

