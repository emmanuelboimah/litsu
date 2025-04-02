from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('litsu-wp/', admin.site.urls),
    
    path('', views.Home_Page, name='home'),

]
