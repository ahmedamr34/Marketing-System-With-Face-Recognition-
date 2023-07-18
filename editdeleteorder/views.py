from django.shortcuts import render, redirect, get_object_or_404
from myorder.models import Order
from .forms import EditOrderForm, DeleteOrderForm


def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        form = EditOrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditOrderForm(instance=order)
    
    return render(request, 'EditOrder.html', {'form': form})

def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)

    if request.method == 'POST':
        form = DeleteOrderForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm_delete']:
            order.delete()
            return redirect('dashboard')
    else:
        form = DeleteOrderForm()

    context = {
        'form': form,
        'order': order,
    }
    return render(request, 'DeleteOrder.html', context)

