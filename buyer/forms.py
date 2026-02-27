from django import forms
from transactions.models import RFQ

class RFQForm(forms.ModelForm):
    class Meta:
        model = RFQ
        fields = ['quantity', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
