from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Django example",
        },
    )

def matches(request):
    
    #return render(request,"matches.html",{"matches": "matches example"})