from django.http import HttpResponse

def home(request):
    return HttpResponse('home page')

def add_department(request):
    return HttpResponse('add_deparment.html')

def add_comp_desc(request):
    return HttpResponse('add_comp_desc.html')

def add_complain_type(request):
    return HttpResponse('add_complain_type.html')

def add_it_team(request):
    return HttpResponse('add_it_team.html')

def add_new_complain(request):
    return HttpResponse('add_new_complain.html')

def add_user(request):
    return HttpResponse('add_user.html')

def change_password(request):
    return HttpResponse('change_password.html')

def complain_report(request):
    return HttpResponse('complain_report.html')

def edit_comp_desc(request):
    return HttpResponse('edit_comp_desc.html')

def edit_complain_type(request):
    return HttpResponse('edit_complain_type.html')

def edit_department(request):
    return HttpResponse('edit_deparment.html')

def Edit_it_team(request):
    return HttpResponse('Edit_it_team.html')

def edit_user(request):
    return HttpResponse('edit_user.html')

def it_team_details(request):
    return HttpResponse('it_team_details.html')

def login(request):
    return HttpResponse('login.html')

def register(request):
    return HttpResponse('register.html')

def user_complain(request):
    return HttpResponse('user_complain.html')

def user_details(request):
    return HttpResponse('user_details.html')

def User_complain_it(request):
    return HttpResponse('User_complain.html')



































