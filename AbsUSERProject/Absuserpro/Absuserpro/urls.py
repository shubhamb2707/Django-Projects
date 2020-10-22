from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('Absuserapp/', include(('Absuserapp.urls', 'Absuserapp'))),
    path('Absuserapp/', include('django.contrib.auth.urls')),
]