from django.shortcuts import render
from .models import sponsor

# Create your views here.
def service_View(request):
    return render(request,'index2.html', {'ser' : sponsor.objects.all()})