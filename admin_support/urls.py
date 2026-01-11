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
from admin_support import views  # Import views from the admin app
urlpatterns = [
   
    path("virtual_assistant/", views.virtual_assistant, name="virtual_assistant"),
    path('',views.SignupPage,name='signup'), # Redirect root URL to admin
    path('login/',views.LoginPage,name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('user_change_password/', views.user_change_password, name='user_change_password'),
    path('/update_password', views.update_password, name='update_password'),

# department
    path('department', views.department, name='department'),  # Redirect root URL to admin
    path('insert_department', views.insert_department, name='insert_department'),
    path('update_department', views.update_department, name='update_department'),
    path('delete_dept/<int:dept_id>', views.delete_dept, name='delete_dept'),    
    path('edit_department/<int:dept_id>',views.edit_department, name='edit_department'),
    path('update_department',views.update_department, name='update_department'),


# user_details
    path('user_details', views.user_details, name='user_details'),
    path('add_user', views.add_user, name='add_user'),
    path('/insert_user', views.insert_user, name='insert_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('/update_user', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

# it_team
    path('it_team_details/', views.it_team_details, name='it_team_details'),
    path('add_it_team/', views.add_it_team, name='add_it_team'),
    path('insert_it_team/', views.insert_it_team, name='insert_it_team'),
    path('edit_it_team/<int:it_team_id>/', views.edit_it_team, name='edit_it_team'),
    path('update_it_team/', views.update_it_team, name='update_it_team'),
    path('delete_it_team/<int:it_team_id>/', views.delete_it_team, name='delete_it_team'),




#complain_type 

    path('add_complain_type/', views.add_complain_type, name='add_complain_type'),
    path('insert_complain_type/', views.insert_complain_type, name='insert_complain_type'),
    path('edit_complain_type/<int:complain_type_id>/', views.edit_complain_type, name='edit_complain_type'),
    path('/update_complain_type', views.update_complain_type, name='update_complain_type'),
    path('delete_complain_type/<int:complain_type_id>/', views.delete_complain_type, name='delete_complain_type'),

# Complain_desc
    path('add_complaint_description/', views.add_complaint_description, name='add_complaint_description'),
    path('insert_complaint_description/', views.insert_complaint_description, name='insert_comp_desc'),
    path('edit_complaint_desc/<int:complain_desc_id>/', views.edit_complaint_description, name='edit_complaint_desc'),
    path('update_complaint_desc/', views.update_complaint_description, name='update_complaint_desc'),
    path('delete_complaint_desc/<int:complain_desc_id>/', views.delete_complaint_description, name='delete_complaint_desc'),

# user_complain
    path('user_complain/', views.user_complain_details, name='user_complain_details'),
    path('add_user_complain/', views.add_user_complain, name='add_user_complain'),
    path('insert_user_complain/', views.insert_user_complain, name='insert_user_complain'),
    path('edit_user_complain/<int:user_complain_id>/', views.edit_user_complain, name='edit_user_complain'),
    path('update_user_complain/', views.update_user_complain, name='update_user_complain'),
    path('delete_user_complain/<int:user_complain_id>/', views.delete_user_complain, name='delete_user_complain'),


#complain_report

    path('complain-report/', views.complain_report, name='complain_report'), 



    #Ajax urls
    path('fetch_user/', views.fetch_user, name='fetch_user'),
    path('fetch_user_email/', views.fetch_user_email, name='fetch_user_email'),
    path('fetch-complain-desc/', views.fetch_complain_desc_by_type, name='fetch_complain_desc_by_type'),




    # complain report date
    # path('fetch_report/', views.fetch_report, name='fetch_report'),

]


    





