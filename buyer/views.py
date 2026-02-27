from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from sawmill.models import Product, Species, Category
from transactions.models import RFQ
from .forms import RFQForm

def product_list(request):
    products = Product.objects.filter(is_active=True)
    species_list = Species.objects.all()
    categories = Category.objects.all()

    # Filtering
    query = request.GET.get('q')
    species_filter = request.GET.get('species')
    category_filter = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if query:
        products = products.filter(
            Q(species__name__icontains=query) |
            Q(dimensions__icontains=query) |
            Q(grade__name__icontains=query)
        )
    
    if species_filter:
        products = products.filter(species__id=species_filter)
    
    if category_filter:
        products = products.filter(category__id=category_filter)

    if min_price:
        products = products.filter(price_per_unit__gte=min_price)
    
    if max_price:
        products = products.filter(price_per_unit__lte=max_price)

    context = {
        'products': products,
        'species_list': species_list,
        'categories': categories,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'buyer/product_list_partial.html', context)

    return render(request, 'buyer/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'buyer/product_detail.html', {'product': product})

@login_required
def rfq_create(request, product_id):
    if request.user.role != 'BUYER':
        messages.warning(request, "Only buyers can request quotes.")
        return redirect('product_detail', pk=product_id)

    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = RFQForm(request.POST)
        if form.is_valid():
            rfq = form.save(commit=False)
            rfq.buyer = request.user
            rfq.product = product
            rfq.save()
            messages.success(request, "Request for Quote sent successfully.")
            return redirect('buyer_dashboard')
    else:
        form = RFQForm()
    
    return render(request, 'buyer/rfq_form.html', {'form': form, 'product': product})
