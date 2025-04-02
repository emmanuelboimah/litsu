from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER = (
        (1,'ADMIN'),
    )
    user_type = models.CharField(choices=USER, max_length=58, default=1)
    
NEWS = "News"
ANNOUNCEMENTS = "Announcements"

CATEGORIES = (
    (NEWS, "News"),
    (ANNOUNCEMENTS, "Announcements"),
)   
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    category = models.CharField(max_length=100, choices=CATEGORIES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Email(models.Model):
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email
    
class Contact_Form(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    contact_message = models.CharField(max_length=100, blank=True, null=True)
    
    
    def __str__(self):
        return self.contact_name
     
class Chapter(models.Model):
    chapters_name = models.CharField(max_length=100)
    chapters_cover = models.ImageField(upload_to='media/chapters/cover')
    
    chairman_name = models.CharField(max_length=100)
    chairman_pic = models.ImageField(upload_to='media/chapters/chairman')
    
    co_chairman_name = models.CharField(max_length=100)
    co_chairman_pic = models.ImageField(upload_to='media/chapters/co_chairman')
    
    secretary_name = models.CharField(max_length=100)
    secretary_pic = models.ImageField(upload_to='media/chapters/secretary')
    
    financial_secretary_name = models.CharField(max_length=100)
    financial_secretary_pic = models.ImageField(upload_to='media/chapters/financial_secretary')
    
    treasurer_name = models.CharField(max_length=100)
    treasurer_pic = models.ImageField(upload_to='media/chapters/treasurer')
    
    chaplain_name = models.CharField(max_length=100)
    chaplain_pic = models.ImageField(upload_to='media/chapters/chaplain')
    
    training_director_name = models.CharField(max_length=100)
    training_director_pic = models.ImageField(upload_to='media/chapters/training_director')
    
    program_director_name = models.CharField(max_length=100)
    program_director_pic = models.ImageField(upload_to='media/chapters/program_director')
    
    parliamentarian_name = models.CharField(max_length=100)
    parliamentarian_pic = models.ImageField(upload_to='media/chapters/parliamentarian')
    
    reporter_name = models.CharField(max_length=100)
    reporter_pic = models.ImageField(upload_to='media/chapters/reporter')
    
    girl_in_ict_name = models.CharField(max_length=100)
    girl_in_ict_pic = models.ImageField(upload_to='media/chapters/girl_in_ict')

    def __str__(self):
        return self.chapters_name


class Leaderships(models.Model):
    president = models.CharField(max_length=100, blank=True, null=True)
    president_cover = models.ImageField(upload_to='media/leadership/cover', blank=True, null=True)
    vic_president = models.CharField(max_length=100, blank=True, null=True)
    vic_president_cover = models.ImageField(upload_to='media/leadership/cover', blank=True, null=True)
    financial_secretary = models.CharField(max_length=100, blank=True, null=True)
    financial_secretary_cover = models.ImageField(upload_to='media/leadership/cover', blank=True, null=True)
    secretary_general = models.CharField(max_length=100, blank=True, null=True)
    secretary_general_cover = models.ImageField(upload_to='media/leadership/cover', blank=True, null=True)
    aLL_chapters_chairman = models.CharField(max_length=100, blank=True, null=True)
    aLL_chapters_chairma_cover = models.ImageField(upload_to='media/leadership/cover', blank=True, null=True)
    program_director = models.CharField(max_length=100, blank=True, null=True)
    program_director_cover = models.ImageField(upload_to='media/leadership/cover', blank=True, null=True)   
    training_director = models.CharField(max_length=100, blank=True, null=True)
    training_director_cover = models.ImageField(upload_to='media/leadership/cover', blank=True, null=True)
    sa = models.CharField(max_length=100, blank=True, null=True)
    sa_cover = models.ImageField(upload_to='media/leadership/cover', blank=True, null=True)
    
    girls_in_ICTs_chairlady = models.CharField(max_length=100, blank=True, null=True)
    girls_in_ICTs_chairlady_cover = models.ImageField(upload_to='media/leadership/cover', blank=True, null=True)
    national_reporter = models.CharField(max_length=100, blank=True, null=True)
    national_reporter_cover = models.ImageField(upload_to='media/leadership/cover', blank=True, null=True)
    systems_administrator = models.CharField(max_length=100, blank=True, null=True)
    systems_administrator_cover = models.ImageField(upload_to='media/leadership/cover', blank=True, null=True)
    p_r_o = models.CharField(max_length=100, blank=True, null=True)
    p_r_o_cover = models.ImageField(upload_to='media/leadership/cover', blank=True, null=True)
     
    year = models.CharField(max_length=100, blank=True, null=True)
       
    def __str__(self):
        return self.year
    
class Chapter_Chairman(models.Model):
    chapter_chairman_name = models.CharField(max_length=200)
    chapter_chairman_cover = models.ImageField(upload_to='media/leadership/cover')
    leadership = models.ForeignKey(Leaderships, on_delete=models.CASCADE) 

    
class Membership_From(models.Model): 
    profile_pic = models.ImageField(upload_to='media/membership/profile_pic')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    home_address = models.TextField()
    birth_date = models.DateField()
    nationality = models.CharField(max_length=100)
    county_of_residence = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    extra_skill = models.CharField(max_length=100)
    level_of_education = models.CharField(max_length=100)
    chapter_name = models.CharField(max_length=100, blank=True)
    living_with = models.CharField(max_length=10)
    working_or_not = models.CharField(max_length=3, blank=True)
    if_yes_place_of_work = models.CharField(max_length=100, blank=True)
    hear_about_us = models.CharField(max_length=100)
    why_be_member = models.TextField()
    emergency_first_name = models.CharField(max_length=100)
    emergency_last_name = models.CharField(max_length=100)
    emergency_email = models.EmailField()
    emergency_address = models.TextField()
    emergency_relationship = models.CharField(max_length=100)
    accepted_membership_rules = models.BooleanField(default=False)
    accepted_privacy_policy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
     
class Advisory(models.Model):
    advisory_name = models.CharField(max_length=100)
    advisory = models.ImageField(upload_to='media/advisory/pic')
    occupation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.advisory_name

class President(models.Model):
    Presidential_info = models.CharField(max_length=100)
    Presidential_image = models.ImageField(upload_to='media/Presidential/pic')
    
    def __str__(self):
        return self.Presidential_info
    
class All_Slider(models.Model):
    slider1_image = models.ImageField(upload_to='media/slider/images')
