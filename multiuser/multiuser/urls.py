from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('classroom/', include('classroom.urls',namespace='classroom')),
    path('admin/',admin.site.urls),
]