from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from .models import Expense
# @admin.register(Expense)
# class ExpenseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'amount', 'date', 'category', 'is_group', 'members')
#     search_fields = ('name', 'category')


from django.contrib import admin
from .models import IndividualExpense, GroupExpense  # Import the correct models

# Admin configuration for IndividualExpense
@admin.register(IndividualExpense)
class IndividualExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date', 'category')  # Don't include 'members' for Individual
    search_fields = ('name', 'category')

# Admin configuration for GroupExpense
@admin.register(GroupExpense)
class GroupExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date', 'category', 'is_group', 'member1', 'member2', 'member3', 'member4', 'member5')
    search_fields = ('name', 'category')

