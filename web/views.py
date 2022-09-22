from django.shortcuts import render,redirect

# Create your views here.
def index(request):

    return render(request,'web/index.html')

def aboutUs(request):

    return render(request,'web/aboutUs.html')


def solutions(request):

    return render(request,'web/solutions.html')

def shop(request):

    return render(request,'web/shop.html')

def contactUs(request):

    return render(request,'web/contactUs.html')

def projects(request):

    return render(request,'web/projects.html')