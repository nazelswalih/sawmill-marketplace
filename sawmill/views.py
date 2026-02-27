from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, SawmillProfile
from .forms import ProductForm, SawmillProfileForm
from .utils import calculate_board_feet
from django.http import JsonResponse

@login_required
def inventory_list(request):
    # Ensure user is a seller
    if request.user.role != 'SELLER':
        return redirect('home')
        
    try:
        profile = request.user.sawmill_profile
    except SawmillProfile.DoesNotExist:
        # Redirect to create profile if not exists (or handle appropriately)
        return redirect('profile_edit')

    products = Product.objects.filter(seller=profile)
    return render(request, 'sawmill/inventory_list.html', {'products': products})

@login_required
def product_add(request):
    if request.user.role != 'SELLER':
        return redirect('home')
        
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user.sawmill_profile
            product.save()
            messages.success(request, 'Product added successfully.')
            return redirect('inventory_list')
    else:
        form = ProductForm()
    return render(request, 'sawmill/product_form.html', {'form': form, 'title': 'Add Product'})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk, seller__user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('inventory_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'sawmill/product_form.html', {'form': form, 'title': 'Edit Product'})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk, seller__user=request.user)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted.')
        return redirect('inventory_list')
    return render(request, 'sawmill/product_confirm_delete.html', {'product': product})

@login_required
def profile_edit(request):
    try:
        profile = request.user.sawmill_profile
    except SawmillProfile.DoesNotExist:
        profile = SawmillProfile(user=request.user)

    if request.method == 'POST':
        form = SawmillProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')
            return redirect('seller_dashboard')
    else:
        form = SawmillProfileForm(instance=profile)
    return render(request, 'sawmill/profile_form.html', {'form': form})

@login_required
def volume_calculator(request):
    result = None
    if request.method == 'POST':
        length = request.POST.get('length', 0)
        width = request.POST.get('width', 0)
        thickness = request.POST.get('thickness', 0)
        quantity = request.POST.get('quantity', 1)
        result = calculate_board_feet(length, width, thickness, quantity)
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'board_feet': result})
            
    return render(request, 'sawmill/volume_calculator.html', {'result': result})

# Simple Admin Views
from .models import Category, Species, Grade
from .forms import CategoryForm, SpeciesForm, GradeForm

@login_required
def manage_resources(request):
    if not (request.user.role == 'ADMIN' or request.user.is_superuser):
        return redirect('home')
        
    categories = Category.objects.all()
    species = Species.objects.all()
    grades = Grade.objects.all()
    
    return render(request, 'sawmill/manage_resources.html', {
        'categories': categories,
        'species': species,
        'grades': grades
    })

@login_required
def resource_action(request, model_name, action, pk=None):
    if not (request.user.role == 'ADMIN' or request.user.is_superuser):
        return redirect('home')
    
    # Map model names to Model classes and Form classes
    model_map = {
        'category': (Category, CategoryForm),
        'species': (Species, SpeciesForm),
        'grade': (Grade, GradeForm),
    }
    
    if model_name not in model_map:
        return redirect('manage_resources')
        
    ModelClass, FormClass = model_map[model_name]
    
    # Handle Delete
    if action == 'delete' and pk:
        item = get_object_or_404(ModelClass, pk=pk)
        if request.method == 'POST':
            item.delete()
            messages.success(request, f'{model_name.title()} deleted successfully.')
            return redirect('manage_resources')
        return render(request, 'sawmill/resource_confirm_delete.html', {'item': item, 'model_name': model_name})

    # Handle Add/Edit
    item = None
    if action == 'edit' and pk:
        item = get_object_or_404(ModelClass, pk=pk)
    
    if request.method == 'POST':
        form = FormClass(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'{model_name.title()} saved successfully.')
            return redirect('manage_resources')
    else:
        form = FormClass(instance=item)
        
    return render(request, 'sawmill/resource_form.html', {
        'form': form, 
        'title': f"{'Edit' if item else 'Add'} {model_name.title()}",
        'model_name': model_name
    })
