from django.db import models
from django.conf import settings

class SawmillProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sawmill_profile')
    business_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, help_text="e.g. 123 Timber Rd, Portland, OR")
    machinery_details = models.TextField(blank=True, help_text="List equipment like band saws, kilns, etc.")
    logo = models.ImageField(upload_to='sawmill_logos/', blank=True, null=True)

    def __str__(self):
        return self.business_name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Species(models.Model):
    name = models.CharField(max_length=100)
    botanical_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Species"

class Grade(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    seller = models.ForeignKey(SawmillProfile, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)
    dimensions = models.CharField(max_length=100, help_text="e.g. 2x4x8")
    moisture_content = models.FloatField(help_text="Percentage (e.g. 12.5)")
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.species} - {self.dimensions}"
