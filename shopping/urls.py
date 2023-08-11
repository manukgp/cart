from django.urls import path

# importing views from views..py
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about', views.home, name='about'),
	path('create/', views.shopping_item_create, name='shopping_item_create'),
    path('list', views.shopping_item_list, name='shopping_item_list'),
	path('detail', views.shopping_item_detail, name='shopping_item_detail'),
	path('update', views.shopping_item_update, name='shopping_item_update'),
	path('delete', views.shopping_item_delete, name= 'shopping_item_delete'),
]
