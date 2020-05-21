from django.shortcuts import render

def home(request):
    return render(request, 'profile_api/home.html')