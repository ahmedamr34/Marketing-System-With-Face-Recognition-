from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from login.models import UserReg
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']
        image = request.FILES.get('image')

        # Check if username or email already exist in the database
        existing_user = UserReg.objects.filter(username=userName).exists()
        existing_email = UserReg.objects.filter(email=email).exists()

        if existing_user:
            messages.error(request, 'Username already exists.')
            return redirect('register')  # Replace 'your_view_name' with the actual name of your view

        if existing_email:
            messages.error(request, 'Email already exists.')
            return redirect('register')  # Replace 'your_view_name' with the actual name of your view
        
        if not image:
            messages.error(request, 'Please select an image.')
            return redirect('register')  # Replace 'your_view_name' with the actual name of your view

        user = UserReg(username=userName, first_name=userName, email=email, password=password, image=image)
        user.save()
        auth_login(request, user)
        return redirect('dashboard')
    else:
        return render(request, 'form login/signup.html')
