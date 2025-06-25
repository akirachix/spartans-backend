from django import forms
from .models import LoanRepayment


class LoanRepaymentForm(forms.ModelForm):
    class Meta:
        model = LoanRepayment
        fields = '__all__'