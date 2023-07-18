from django.shortcuts import render, redirect
from .models import RequestForContact
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        Message = request.POST.get('Message')

        if not Name or not Email or not Message:
            messages.error(request, 'Please fill in all required fields.')
            return redirect('contact')
        else:
            # Create a new ContactMessage instance and save it to the database
            new_message = RequestForContact(name=Name, email=Email, phone=Phone, message=Message)
            new_message.save()
            messages.success(request, 'Message sent successfully, We will contact you as soon as possible!')
            return redirect('contact')
    return render(request, 'contactus.html')