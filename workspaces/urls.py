from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('litsu-wp/', admin.site.urls),
    
    path('', views.Home_Page, name='home'),
    path('chapters/ <str:id>', views.Chapters, name='chapters'),
    path('news updates', views.News, name='news'),
    path('news/ <str:id>', views.News_Detalte, name='news_detalte'),
    path('membership form', views.Membership_Form, name='membership_form'),
    path('about us', views.About_Us, name='about_us'),
    path('contact us', views.Contact_Us, name='contact_us'),
    path('leadership/ <str:id>', views.Leadership, name='leadership'),

]
