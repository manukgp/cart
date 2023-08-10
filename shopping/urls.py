from django.urls import path

# importing views from views..py
from . import views

urlpatterns = [
	path('', views.shopping_item_create),
    path('', views.shopping_item_list),
	path('', views.shopping_item_detail),
	path('', views.shopping_item_update),
	path('', views.shopping_item_delete),
]
