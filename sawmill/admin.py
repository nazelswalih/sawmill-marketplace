from django.contrib import admin
from .models import SawmillProfile, Product, Category, Species, Grade

@admin.register(SawmillProfile)
class SawmillProfileAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'user', 'location')
    search_fields = ('business_name', 'location')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'botanical_name')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('species', 'dimensions', 'grade', 'price_per_unit', 'is_active')
    list_filter = ('species', 'grade', 'is_active', 'category')
