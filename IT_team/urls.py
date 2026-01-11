"""
URL configuration for it_support project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from IT_team import views  # Import views from the admin app

urlpatterns = [
    # path('',views.SignupPage,name='signup'), # Redirect root URL to admin
    path('login/',views.LoginPage,name='IT/login'),
    path('logout/', views.LogoutPage, name='IT/logout'),
    path('change_password_it/', views.change_password_it, name='IT/change_password_it'),
    path('update_password/', views.update_password, name='IT/update_password'),
    path('', views.index, name='index'),  # Redirect root URL to admin
    path('edit_profile/', views.edit_profile, name='IT/edit_profile'),
    path('user_complain_it/', views.user_complain_it, name='IT/user_complain'),
    path('update_user_complain/<int:user_complain_id>', views.update_user_complain, name='update_user_complain'),

    
]
