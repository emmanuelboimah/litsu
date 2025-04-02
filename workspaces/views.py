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