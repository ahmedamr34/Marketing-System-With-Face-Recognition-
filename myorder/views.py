from django.shortcuts import redirect, render
from login.models import UserReg
from websites.models import Place,AddHolder
from .models import Order,Category
from django.contrib import messages
from .forms import orderForm
# Create your views here.

def order_view(request):
    websites = AddHolder.objects.all()
    categories = Category.objects.all()
    context = {'websites': websites, 'categories': categories}
    
    if request.method == 'POST':
        form = orderForm(request.POST, request.FILES)
        if form.is_valid():
            addholder_name = form.cleaned_data['AddHolder_name']
            place = form.cleaned_data['place']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Check if an order with the same AddHolder name and place exists
            existing_order = Order.objects.filter(AddHolder_name=addholder_name, place=place).first()
            if existing_order:
                if existing_order.start_date <= start_date <= existing_order.end_date or existing_order.start_date <= end_date <= existing_order.end_date:
                    error_message = f"The place is occupied between {existing_order.start_date} and {existing_order.end_date}."
                    messages.error(request, error_message)
                    return redirect('order')
            
            form.save()
            messages.success(request, 'Order made successfully!')
            return redirect('dashboard')
    else:
        form = orderForm()
    
    return render(request, 'orderform.html', context={'form': form, **context})





