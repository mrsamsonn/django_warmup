from django.shortcuts import render

def homepage_home(request):
    return render(request, 'homepage/homapage.html')
