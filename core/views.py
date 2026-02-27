from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from transactions.models import RFQ
from sawmill.models import SawmillProfile

def home(request):
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    user = request.user
    if user.role == 'ADMIN' or user.is_superuser:
        return redirect('admin_dashboard')
    elif user.role == 'SELLER':
        return redirect('seller_dashboard')
    elif user.role == 'BUYER':
        return redirect('buyer_dashboard')
    return redirect('home')

from users.models import User
from sawmill.models import Product, SawmillProfile
from transactions.models import RFQ
from itertools import chain
from operator import attrgetter

def admin_dashboard(request):
    # Statistics
    total_users = User.objects.count()
    active_listings = Product.objects.filter(is_active=True).count()
    pending_verification = User.objects.filter(is_verified=False).exclude(role='ADMIN').count()

    # Recent Activity
    recent_users = User.objects.order_by('-date_joined')[:5]
    recent_products = Product.objects.order_by('-created_at')[:5]
    recent_rfqs = RFQ.objects.order_by('-created_at')[:5]

    # Combine and sort activity
    activity_list = sorted(
        chain(recent_users, recent_products, recent_rfqs),
        key=lambda instance: instance.date_joined if isinstance(instance, User) else instance.created_at,
        reverse=True
    )[:10]

    context = {
        'total_users': total_users,
        'active_listings': active_listings,
        'pending_verification': pending_verification,
        'recent_activity': activity_list,
    }
    return render(request, 'core/admin_dashboard.html', context)

@login_required
def seller_dashboard(request):
    try:
        profile = request.user.sawmill_profile
        products = profile.products.all()
        # Get RFQs for these products
        rfqs = RFQ.objects.filter(product__in=products).order_by('-created_at')
    except (SawmillProfile.DoesNotExist, AttributeError):
        products = []
        rfqs = []
    return render(request, 'core/seller_dashboard.html', {'products': products, 'rfqs': rfqs})

@login_required
def buyer_dashboard(request):
    rfqs = request.user.rfqs.all().order_by('-created_at')
    return render(request, 'core/buyer_dashboard.html', {'rfqs': rfqs})
