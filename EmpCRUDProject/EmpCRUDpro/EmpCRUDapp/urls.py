from django.conf.urls import url
from django.contrib import admin
from EmpCRUDapp import views
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('create/', views.CreateView, name="create"),
    path('index/', views.IndexView, name = "index"),
    path('delete/<str:fname>/', views.DeleteView, name="delete"),
    path('update/<str:fname>/', views.UpdateView, name="update"),
    path("", views.Loginview, name="login")
    
]


