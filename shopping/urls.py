from django.urls import path

# importing views from views..py
from . import views

urlpatterns = [
	path('', views.home, name='shopping_home'),
	path('about', views.about, name='shopping_about'),
	path('create', views.shopping_item_create, name='shopping_item_create'),
    path('list', views.shopping_item_list, name='shopping_item_list'),
	path('detail', views.shopping_item_detail, name='shopping_item_detail'),
	path('update', views.shopping_item_update, name='shopping_item_update'),
	path('delete', views.shopping_item_delete, name= 'shopping_item_delete'),
]
