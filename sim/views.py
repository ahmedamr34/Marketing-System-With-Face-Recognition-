from django.shortcuts import render
from myorder.models import Order

def sim_view(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'sim.html',context)
