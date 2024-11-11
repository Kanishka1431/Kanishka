from django.shortcuts import render

def home(request):
    return render(request, 'app_14_3/home.html')