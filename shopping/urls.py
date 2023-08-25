from django.urls import path, include
from .views import ItemListView, ItemDetailView
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import ShoppingItemViewSet

router = routers.DefaultRouter()
router.register(r'items', views.ShoppingItemViewSet)

urlpatterns = [
	path('', ItemListView.as_view(), name='shopping_home'),
    path('list/', ItemListView.as_view(), name='item_list'),
	path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
	path('create/', views.shopping_item_create, name='item_form'),
	path('update/<int:pk>/', views.shopping_item_update, name='item_update'),
	path('delete/<int:pk>/', views.shopping_item_delete, name='item_delete'),
	path('about/', views.about, name='shopping_about'),
    
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
