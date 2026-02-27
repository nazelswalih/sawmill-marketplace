from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('buyer-dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
]
