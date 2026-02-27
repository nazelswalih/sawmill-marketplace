from django import forms
from .models import Category, Species, Grade, Product, SawmillProfile

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['seller', 'created_at', 'updated_at']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class SawmillProfileForm(forms.ModelForm):
    class Meta:
        model = SawmillProfile
        exclude = ['user']
        widgets = {
            'machinery_details': forms.Textarea(attrs={'rows': 3}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class SpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = '__all__'

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
