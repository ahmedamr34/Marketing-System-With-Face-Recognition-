import face_recognition
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
import numpy as np
from PIL import Image
from .models import UserReg
from django.contrib import messages
import io, base64



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        uploaded_image = request.POST.get('captured_image')
        if ';base64,' in uploaded_image:
             _, base64_str = uploaded_image.split(';base64,')
        else:
            # Handle the case when the delimiter is not found
            base64_str = uploaded_image
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))
        img.save('my-image.png')

        if not img:
            messages.error(request, 'Please select an image.')
            return redirect('login')  # Replace 'your_view_name' with the actual name of your view

        try:
            user = UserReg.objects.get(email=email,password=password)
        except UserReg.DoesNotExist:
            messages.error(request, 'invalid email or password.')
            return redirect('login')
        # Load the image from the user object
        known_image = face_recognition.load_image_file(user.image.path)
         # Read the uploaded image and convert it to a NumPy array
        img_rgb=img.convert('RGB')
        uploaded_image_array = np.array(img_rgb)
        # Encode the images
        try:
            uploaded_image_encoding = face_recognition.face_encodings(uploaded_image_array)[0]
            known_image_encoding = face_recognition.face_encodings(known_image)[0]
            # Compare the uploaded image with the image in the user object
            results = face_recognition.compare_faces([known_image_encoding], uploaded_image_encoding)
        except :
            messages.error(request, 'There is a problem with this image, Please select another one with your face clear!')
            return redirect('login')
        
        if results[0]:
            # Save the user object in the session
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Face not recognized.')
            return redirect('login')
    else:
        return render(request, 'form login/login.html')
    

def logout_View(request):
    logout(request)
    return redirect('home')



