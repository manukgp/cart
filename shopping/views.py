from django.shortcuts import render, redirect, get_object_or_404
from .models import ShoppingItem
from .forms import ShoppingForm
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView
from users.decorators import superuser_required

from shopping.serializers import ShoppingItemSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics

def home(request):
    items = ShoppingItem.objects.all()
    return render(request, 'shopping/home.html', {'items':items})

def about(request):
    return render(request, 'shopping/about.html')

class ItemListView(ListView):
    model = ShoppingItem
    template_name = 'shopping/home.html'
    context_object_name = 'items'

class ItemDetailView(DetailView):
    model = ShoppingItem
    template_name = 'shopping/item_detail.html'

@superuser_required
def shopping_item_create(request):
    form = ShoppingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'shopping/item_form.html', {'form': form})

@superuser_required
def shopping_item_update(request, pk):
    if request.user.is_superuser:
        items = get_object_or_404(ShoppingItem, pk=pk)
        form = ShoppingForm(request.POST or None, instance=items)
        # form = ShoppingForm(request.POST or None, files=request.FILES, instance=items)
        form.image = request.FILES.get('image')     
        print('new',form)

        if form.is_valid():
            form.save()
            return redirect('item_detail', pk=pk)
    return render(request, 'shopping/item_form.html', {'form': form})

@superuser_required
def shopping_item_delete(request, pk):
    if request.user.is_superuser:
        items = get_object_or_404(ShoppingItem, pk=pk)
        if request.method == 'POST':
            items.delete()
            return redirect('item_list')
    return render(request, 'shopping/item_delete.html', {'item': items})

class ShoppingItemViewSet(viewsets.ModelViewSet):

    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer
    permission_classes = [permissions.IsAuthenticated]

# class ShoppingItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ShoppingItem.objects.all()
#     serializer_class = ShoppingItemSerializer