from django.shortcuts import render
from .models import portfolio

# Create your views here.
def portfolio_View(request):
    return render(request,'portfolio.html', {'por' : portfolio.objects.all()})