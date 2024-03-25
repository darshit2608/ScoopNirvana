from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

def index(request):
    #messages.success(request, "This is a test message.")
    return render(request, 'index.html')

def about(request):
    # Define the context before rendering the template
    context = {}
    return render(request, 'about.html', context)

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        # Validate form data before saving
        if name and email and phone and desc:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Please fill in all the fields.')
    
    return render(request, 'contact.html')

