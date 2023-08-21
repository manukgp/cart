from django.shortcuts import render, redirect, get_object_or_404
from .models import ShoppingItem
from .forms import ShoppingForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, DeleteView

def home(request):
    items = ShoppingItem.objects.all()
    return render(request, 'shopping/home.html', {'items':items})

class ItemListView(ListView):
    model = ShoppingItem
    template_name = 'shopping/home.html'
    context_object_name = 'items'
    ordering = [ 'item' ]    

class ItemDetailView(DetailView):
    model = ShoppingItem
    # template_name = 'shopping/shopping_item_detail.html'
    # context_object_name = 'items'


def about(request):
    return render(request, 'shopping/about.html')

def shopping_item_list(request):
    items = ShoppingItem.objects.all()
    return render(request, 'shopping/shopping_item_list.html', {'items': items})

def shopping_item_detail(request, pk):
    items = get_object_or_404(ShoppingItem, pk=pk)
    return render(request, 'shopping/shopping_item_detail.html', {'item': items})

def shopping_item_create(request):
    form = ShoppingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('shopping_item_list')
    return render(request, 'shopping/shopping_item_form.html', {'form': form})
    # return HttpResponse("account created")

def shopping_item_update(request, pk):
    items = get_object_or_404(ShoppingItem, pk=pk)
    form = ShoppingForm(request.POST or None, instance=items)
    if form.is_valid():
        form.save()
        return redirect('shopping_item_list')
    return render(request, 'shopping/shopping_item_form.html', {'form': form})

def shopping_item_delete(request, pk):
    items = get_object_or_404(ShoppingItem, pk=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('shopping_item_list')
    return render(request, 'shopping/shopping_item_confirm_delete.html', {'item': items})