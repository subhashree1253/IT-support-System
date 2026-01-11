from django.contrib import admin

from .models import AdminLogin, DepartmentDetails, ITTeam, ComplaintDescription,ComplaintType,UserDetails,UserComplain

admin.site.register(AdminLogin)
admin.site.register(DepartmentDetails)
admin.site.register(ITTeam)
admin.site.register(ComplaintDescription)
admin.site.register(ComplaintType)
admin.site.register(UserDetails)
admin.site.register(UserComplain)







# Register your models here.
