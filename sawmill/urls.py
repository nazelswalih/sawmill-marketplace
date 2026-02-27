from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('profile/', views.profile_edit, name='profile_edit'),
    path('calculator/', views.volume_calculator, name='volume_calculator'),
    
    # Resource Management
    path('resources/', views.manage_resources, name='manage_resources'),
    path('resources/<str:model_name>/<str:action>/', views.resource_action, name='resource_add'),
    path('resources/<str:model_name>/<str:action>/<int:pk>/', views.resource_action, name='resource_action'),
]
