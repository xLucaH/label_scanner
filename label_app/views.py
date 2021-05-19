from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def search_label(request):
    return render(request, 'search_label.html')


def label_details(request):
    return render(request, 'label_details.html')

