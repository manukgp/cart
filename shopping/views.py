from django.shortcuts import render, redirect, get_object_or_404
from .models import ShoppingItem
from .forms import ShoppingForm

def create_view(request): 
    context ={} 
  
    form = ShoppingForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
          
    context['form']= form 
    return render(request, "create_view.html", context)

def shopping_item_list(request):
    items = ShoppingItem.objects.all()
    return render(request, 'shopping_item_list.html', {'items': items})

def shopping_item_detail(request, pk):
    item = get_object_or_404(ShoppingItem, pk=pk)
    return render(request, 'shopping_item_detail.html', {'item': item})

def shopping_item_create(request):
    form = ShoppingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('shopping_item_list')
    return render(request, 'shopping_item_form.html', {'form': form})

def shopping_item_update(request, pk):
    item = get_object_or_404(ShoppingItem, pk=pk)
    form = ShoppingForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('shopping_item_list')
    return render(request, 'shopping_item_form.html', {'form': form})

def shopping_item_delete(request, pk):
    item = get_object_or_404(ShoppingItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('shopping_item_list')
    return render(request, 'shopping_item_confirm_delete.html', {'item': item})