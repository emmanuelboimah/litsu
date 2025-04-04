from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('litsu-wp/', admin.site.urls),
    
    path('', views.Home_Page, name='home'),
    path('chapters/ <str:id>', views.Chapters, name='chapters'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)