from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def search_label(request):
    x = 2

    return render(request, 'home.html')