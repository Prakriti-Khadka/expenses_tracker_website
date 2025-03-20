from django import forms
from .models import IndividualExpense, GroupExpense

# Form for Individual Expenses
class IndividualExpenseForm(forms.ModelForm):
    class Meta:
        model = IndividualExpense
        fields = ['name', 'amount', 'date', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

# Form for Group Expenses
class GroupExpenseForm(forms.ModelForm):
    class Meta:
        model = GroupExpense
        fields = ['name', 'amount', 'date', 'category', 'member1', 'member2', 'member3', 'member4', 'member5']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
