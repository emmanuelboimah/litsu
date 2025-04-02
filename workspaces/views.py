from django.shortcuts import render, redirect



def LOGIN(request):
    return render(request, 'settings/login.html')