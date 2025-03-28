from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib import admin
from .models import IndividualExpense, GroupExpense  # Import the correct models

# Admin configuration for IndividualExpense
@admin.register(IndividualExpense)
class IndividualExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date', 'category') 
    search_fields = ('name', 'category')

# Admin configuration for GroupExpense
# @admin.register(GroupExpense)
# class GroupExpenseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'amount', 'date', 'category', 'is_group', 'member1', 'member2', 'member3', 'member4', 'member5')
#     search_fields = ('name', 'category')

class GroupExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date', 'category', 'display_members')

    def display_members(self, obj):
        return ", ".join(member.name for member in obj.members.all()) if obj.members.exists() else "No Members"

    display_members.short_description = "Members"

admin.site.register(GroupExpense, GroupExpenseAdmin)



