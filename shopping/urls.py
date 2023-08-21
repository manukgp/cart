from django.urls import path
from .views import ItemListView, ItemDetailView
from . import views

urlpatterns = [
	path('', ItemListView.as_view(), name='shopping_home'),
	path('create', views.shopping_item_create, name='shopping_item_create'),
    path('list', views.shopping_item_list, name='shopping_item_list'),
	path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
	path('update', views.shopping_item_update, name='shopping_item_update'),
	path('delete', views.shopping_item_delete, name= 'shopping_item_delete'),
	path('about', views.about, name='shopping_about'),
]
