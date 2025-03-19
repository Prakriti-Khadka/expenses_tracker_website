"""
URL configuration for expenses_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views  # Import the login view
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views

from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.index, name='index'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-login/', views.admin_login, name='admin_login'),
    # path('logout/', views.custom_logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login URL
   path('admin-expense/edit/<int:expense_id>/<str:is_group>/', views.admin_expense_edit, name='admin_expense_edit'),
   path('admin-expense/delete/<int:expense_id>/<str:is_group>/', views.admin_expense_delete, name='admin_expense_delete'),
    path('add-expense/', views.add_expense, name='add_expense'),

    
    # //Extra
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    # path('logout/', views.user_logout, name='user_logout'),
    # path('register/', views.register, name='register'),
    #  path('login/', views.user_login, name='login'),
    # path('login/', views.CustomLoginView.as_view(), name='login'),
    # path('logout/', views.user_logout, name='logout'),
    path('index/', views.index, name='index'), 



path('admin-logout/', views.custom_logout, name='admin_logout'),
path('user-logout/', views.user_logout, name='user_logout'),

]





