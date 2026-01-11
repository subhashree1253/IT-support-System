from django.contrib import admin
from django.urls import path, include
from admin_support import views
from IT_team import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
   # path('add_department/', views.add_department),
    path('', include('admin_support.urls')), 
    path('it_team/', include('IT_team.urls')), 
]