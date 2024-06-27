from django import forms
from .models import Book, Borrow

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['borrowed_date', 'return_date']
        widgets = {
            'borrowed_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }