from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from .models import IndividualExpense, GroupExpense
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def custom_logout(request):
    logout(request)
    # return redirect('index')
    return redirect('login')

# Function to check if user is a superuser
def is_superuser(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(is_superuser, login_url='admin_login')  # Restrict non-superusers
def admin_dashboard(request):
    # Fetch both individual and group expenses
    personal_expenses = IndividualExpense.objects.all()
    group_expenses = GroupExpense.objects.all()
    users = User.objects.all()


    context = {
        'personal_expenses': personal_expenses,
        'group_expenses': group_expenses,
         'users': users,
    }

    return render(request, 'admin_dashboard.html', context)

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("admin_dashboard")
        else:
            return render(request, "admin_login.html", {"error": "Invalid credentials or not an admin."})

    return render(request, "admin_login.html")


@user_passes_test(is_superuser, login_url='admin_login')
def admin_expense_edit(request, expense_id, is_group):
    # Convert is_group to a boolean
    is_group = True if is_group.lower() == 'true' else False

    # Check if the expense is individual or group and fetch the correct model
    if is_group:
        expense = get_object_or_404(GroupExpense, id=expense_id)
    else:
        expense = get_object_or_404(IndividualExpense, id=expense_id)

    # Handle form submission (POST request)
    if request.method == "POST":
        expense.name = request.POST.get("name")
        expense.amount = request.POST.get("amount")
        expense.date = request.POST.get("date")
        expense.category = request.POST.get("category")

        # Handle group expense members if it's a group expense
        if is_group:
            expense.member1 = request.POST.get("member1")
            expense.member2 = request.POST.get("member2")
            expense.member3 = request.POST.get("member3")
            expense.member4 = request.POST.get("member4")
            expense.member5 = request.POST.get("member5")

        # Save the updated expense
        expense.save()

        return redirect('admin_dashboard')  # Redirect to the dashboard after saving

    # Render the edit form with the current expense data if it's a GET request
    return render(request, 'admin_expense_edit.html', {'expense': expense, 'is_group': is_group})

@user_passes_test(is_superuser, login_url='admin_login')
def admin_expense_delete(request, expense_id, is_group):
    # Convert is_group to a boolean
    is_group = True if is_group.lower() == 'true' else False

    # Delete the expense based on whether it's individual or group
    if is_group:
        expense = get_object_or_404(GroupExpense, id=expense_id)
    else:
        expense = get_object_or_404(IndividualExpense, id=expense_id)

    expense.delete()
    return redirect('admin_dashboard')

# @csrf_exempt  # Allow this view to be called from a non-CSRF-safe environment like JavaScript
# def add_expense(request):
#     if request.method == "POST":
#         try:
#             # Parse incoming JSON data
#             data = json.loads(request.body)

#             # Extract fields from the incoming data
#             name = data.get('name')
#             amount = data.get('amount')
#             date = data.get('date')
#             category = data.get('category')
#             is_group = data.get('is_group')
#             members = data.get('members') if is_group else None

#     #         # Create the expense based on whether it's an individual or group
#             if is_group:
#                 expense = GroupExpense.objects.create(
#                     name=name,
#                     amount=amount,
#                     date=date,
#                     category=category,
#                     is_group=is_group,
#                     member1=members[0] if len(members) > 0 else None,
#                     member2=members[1] if len(members) > 1 else None,
#                     member3=members[2] if len(members) > 2 else None,
#                     member4=members[3] if len(members) > 3 else None,
#                     member5=members[4] if len(members) > 4 else None,
#                 )
#             else:
#                 expense = IndividualExpense.objects.create(
#                     name=name,
#                     amount=amount,
#                     date=date,
#                     category=category,
#                 )

#             # Return a successful response
#             return JsonResponse({'success': True, 'message': 'Expense added successfully!'})

#         except Exception as e:
#             # Log the error and return an error response
#             print(f"Error: {e}")
#             return JsonResponse({'success': False, 'message': 'Error adding expense. Please try again.'})

#     return JsonResponse({'success': False, 'message': 'Invalid request method.'})

import json
from django.http import JsonResponse
from .models import IndividualExpense

def add_personal_expense(request):
    if request.method == "POST":
        try:
            # Parse incoming JSON data
            data = json.loads(request.body)

            # Extract the fields from the incoming data
            name = data.get('name')
            amount = data.get('amount')
            date = data.get('date')
            category = data.get('category')

            # Create the personal expense in the database
            expense = IndividualExpense.objects.create(
                name=name,
                amount=amount,
                date=date,
                category=category,
            )

            # Return a successful response
            return JsonResponse({'success': True, 'message': 'Personal expense added successfully!'})

        except Exception as e:
            # Log the error and return an error response
            print(f"Error: {e}")
            return JsonResponse({'success': False, 'message': 'Error adding personal expense. Please try again.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})




def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            # Display form errors
            errors = form.errors.as_json()
            print(errors)  # For debugging, you can remove this later
            messages.error(request, 'Registration failed.')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'This account is not registered.')
            return redirect('login')
    return render(request, 'login.html')

    # return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')


def admin_user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'admin_user_edit.html', {'user': user})

def admin_user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # Prevent superusers from deleting themselves
    if user.is_superuser:
        messages.error(request, "You cannot delete a superuser.")
        return redirect('admin_dashboard')

    user.delete()
    messages.success(request, "User deleted successfully.")
    return redirect('admin_dashboard')