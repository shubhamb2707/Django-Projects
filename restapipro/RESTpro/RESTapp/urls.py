
from django.urls import path
from . import views

urlpatterns = [
    path("Student/",views.Student_list),
]
