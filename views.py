from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    names = ["Mary", "Billy", "Maxine","Bruce"]
    context = {
        'names':names,
    }
    return render(request,"home.html", context)