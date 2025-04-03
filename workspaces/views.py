from django.shortcuts import render, redirect
from itertools import chain
from django.shortcuts import redirect, render
from app.models import*
from django.contrib import messages


def Home_Page(request):
    blogs = Post.objects.all().order_by('-created_at')[:4]
    chapters = Chapter.objects.all()
    leaderships = Leaderships.objects.all().order_by('-id')
    view_slid = All_Slider.objects.all()
    view_prsident = President.objects.all()
       
    chapters_count = Chapter.objects.all().count()
    membership_count = Membership_From.objects.all().count()

    context = {
        'blogs': blogs, 
        'chapters': chapters,
        'chapters_count': chapters_count,
        'membership_count': membership_count,
        'leaderships': leaderships,
        'view_prsident': view_prsident,
        'view_slid': view_slid,
    }
    return render(request, 'pages/indext.html', context)

def Chapters(request, id):
    chapter = Chapter.objects.get(id=id) 
    chapters = Chapter.objects.all()
    leaderships = Leaderships.objects.all().order_by('-id')
    
    context = { 
        'leaderships': leaderships,
        'chapter': chapter,
        'chapters': chapters
    }
    return render(request, 'pages/chapters.html', context)

# ----------------------- Leadership -----------------------
def Leadership(request, id):
    leadership = Leaderships.objects.get(id=id)
    chapters = Chapter.objects.all()
    leaderships = Leaderships.objects.all().order_by('-id')

    # Retrieve chapter chairmen associated with the specific leadership instance
    chapter_chairmen = Chapter_Chairman.objects.filter(leadership=leadership)

    context = { 
        'leaderships': leaderships,
        'leadership': leadership,
        'chapters': chapters,
        'chapter_chairmen': chapter_chairmen,  # Include chapter chairmen in the context
    }
    return render(request, 'pages/leadership.html', context)

# ------------------------ News And Update -------------------
def News(request):
    blogs = Post.objects.all().order_by('-id')
    post = Post.objects.all().order_by('-created_at')[:4]
    chapters = Chapter.objects.all()
    leaderships = Leaderships.objects.all().order_by('-id')

    if request.method == "POST":
        email = request.POST.get('email')
        add_email = Email(
            email=email,
        )
        add_email.save()
        messages.success(request, 'Thank you for Subscribeing')
        return redirect('news')
    
    
    context = { 
        'leaderships': leaderships,
        'blogs': blogs,
        'post': post, 
        'chapters': chapters 
    }
    return render(request, 'pages/news.html', context)

def News_Detalte(request, id):
    blogs_detalte = Post.objects.get(id=id)
    post = Post.objects.all().order_by('-created_at')[:4]
    chapters = Chapter.objects.all()
    leaderships = Leaderships.objects.all().order_by('-id')
    
    char_limit = 500  # For example, 500 characters per "page"
    content = blogs_detalte.content

    # Split the content into chunks
    pages = [content[i:i + char_limit] for i in range(0, len(content), char_limit)]
    
    
    context = { 
        'blogs_detalte': blogs_detalte,
        'post': post,
        'pages': pages,
        'chapters': chapters,
        'leaderships': leaderships
    }
    return render(request, 'pages/news_details.html', context)

# ----------------------- Membership ------------------------
def Membership_Form(request):
    post = Post.objects.all().order_by('-created_at')[:4]
    chapters = Chapter.objects.all()
    leaderships = Leaderships.objects.all().order_by('-id')
    
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name'),
        last_name = request.POST.get('last_name'),
        gender = request.POST.get('gender'),
        phone_number = request.POST.get('phone_number'),
        email = request.POST.get('email'),
        home_address = request.POST.get('home_address'),
        birth_date = request.POST.get('birth_day'),  # Ensure the name matches the input
        nationality = request.POST.get('nationality'),
        county_of_residence = request.POST.get('county_of_origin'),
        occupation = request.POST.get('occupation'),
        extra_skill = request.POST.get('extra_skill'),
        level_of_education = request.POST.get('level_of_education'),
        chapter_name = request.POST.get('chapter_name'),
        
        living_with = request.POST.get('liveing_with'),
        working_or_not = request.POST.get('working_or_not', ''),
        if_yes_place_of_work = request.POST.get('if_yes_place_of_work', ''),
        hear_about_us = request.POST.get('hear_about_us'),
        why_be_member = request.POST.get('why_be_member'),
        emergency_first_name = request.POST.get('emergency_first_name'),
        emergency_last_name = request.POST.get('emergency_last_name'),
        emergency_email = request.POST.get('emergency_email'),
        emergency_address = request.POST.get('emergency_address'),
        emergency_relationship = request.POST.get('emergency_relationship'),
        accepted_membership_rules = 'accepted_membership_rules' in request.POST,
        accepted_privacy_policy = 'accepted_privacy_policy' in request.POST,  
              
    
    
    context = { 
        'leaderships': leaderships,
        'post': post, 
        'chapters': chapters 
    }
    return render(request, 'pages/membership_form.html', context)

# ------------------------ About US ----------------------------
def About_Us(request):
    chapters = Chapter.objects.all()
    advisory = Advisory.objects.all()
    leaderships = Leaderships.objects.all().order_by('-id')
    
    context = { 
        'leaderships': leaderships,
        'chapters': chapters,
        'advisory': advisory,  
    }
    return render(request, 'pages/about_us.html', context)

# ----------------------- Contact US -----------------------
def Contact_Us(request):
    chapters = Chapter.objects.all()
    leaderships = Leaderships.objects.all().order_by('-id')
    
    if request.method == "POST":
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_message = request.POST.get('contact_message')
        
        contact_person = Contact_Form(
            contact_name = contact_name,
            contact_email = contact_email,
            contact_message = contact_message,
        )
        contact_person.save()
        messages.success(request, "Thank you for contacting us, We'll get back to you in 1-2 business days.")
        return redirect('contact_us')
    
    
    
    context = { 
        'leaderships': leaderships,
        'chapters': chapters
        
    }
    return render(request, 'pages/contact_us.html', context)

def Chapters(request, id):
    chapter = Chapter.objects.get(id=id) 
    chapters = Chapter.objects.all()
    leaderships = Leaderships.objects.all().order_by('-id')
    
    context = { 
        'leaderships': leaderships,
        'chapter': chapter,
        'chapters': chapters
    }
    return render(request, 'pages/chapters.html', context)