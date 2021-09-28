from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include ('presentation.urls')),
    path('admin/', admin.site.urls),
]
