from django import forms
from .models import Book, Borrow

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['borrowed_date', 'return_date']