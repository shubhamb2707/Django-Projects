"""from django.contrib import admin
from django.urls import path
from lastapp import views
urlpatterns = [
	path("teacher", views.teacher_profile, name ="teacher"),
	path("student", views.student_profile, name ="student"),
	path('admin/', admin.site.urls),
]"""

from django.contrib import admin
from django.urls import path
from lastapp import views
urlpatterns = [
	#path("teacher", views.teacher_profile_view, name ="teacher"),
	path("student", views.Student_Profile_View, name ="student"),
	path('admin/', admin.site.urls),
]