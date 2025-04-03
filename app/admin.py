from django.contrib import admin
from .models import*
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username','user_type']
    
class Chapter_Chairman_TabularInline(admin.TabularInline):
    model = Chapter_Chairman

class Leaderships_admin(admin.ModelAdmin):
    inlines = [Chapter_Chairman_TabularInline]

admin.site.register(Leaderships, Leaderships_admin)

admin.site.register(CustomUser,UserModel)
admin.site.register(Post)
admin.site.register(Email)
admin.site.register(Chapter)
admin.site.register(Advisory)
admin.site.register(Contact_Form)
admin.site.register(President)
admin.site.register(All_Slider)