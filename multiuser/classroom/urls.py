from django.urls import path
from . import views
app_name = 'classroom'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('student_register/',views.student_registration,name='student_register'),
    path('teacher_register/',views.teacher_registration,name='teacher_register'),
    path('welcome/',views.welcome,name='welcome'),
]