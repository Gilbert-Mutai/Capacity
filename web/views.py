from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Testimonial,Faqs,Contact
from django.contrib import messages

# Create your views here.
def index(request):

     testimonials= Testimonial.objects.all()
     context={
        'testimonials': testimonials
        }

     return render(request,'web/index.html',context)

def aboutUs(request):

    return render(request,'web/aboutUs.html')


# def solutions(request):

#     return render(request,'web/solutions.html')

def shop(request):

    return render(request,'web/shop.html')

def contactUs(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        new_contact = Contact(f_name=f_name, l_name=l_name, email=email, phone=phone, message=message)
        new_contact.save()

        messages.success(request,"Message sent successfully")

    # Faqs
    faqs= Faqs.objects.all()
    context={
        # 'new_contact': new_contact,
        'faqs': faqs
        }

   
    return render(request,'web/contactUs.html',context)

def projects(request):

    return render(request,'web/projects.html')