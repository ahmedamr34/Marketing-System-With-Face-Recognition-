from django.shortcuts import render


# Create your views here.
def aboutus_View(request):
    return render(request,'aboutus.html')