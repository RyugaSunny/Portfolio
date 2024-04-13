from django.shortcuts import render

# Create your views here.
def index(r):
    return render(r,r"portfolio/index.html")

def oldindex(r):
    return render(r,r"oldwebsite/index.html")

def todohome(r):
    return render(r,r"listodo/index.html")