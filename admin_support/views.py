from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import DepartmentDetails,ITTeam,ComplaintType,UserComplain,UserDetails,AdminLogin,ComplaintDescription
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth import update_session_auth_hash
from django.utils.dateparse import parse_date
from datetime import date, datetime
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse






def index(request):
    return render(request,'add_department.html')



def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Passwords do not match")

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username has been created successfully")

        my_user = User.objects.create_user(username, email, pass1)
        my_user.save()

        print(username, email)  # Logging, optional
        return redirect('login')  # Or use HttpResponse if you're not ready yet

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('department')  # Replace with your app's landing page
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')  # Replace 'login' with your desired redirect target




def user_change_password(request):
    
        

    return render(request, 'change_password.html')


def update_password(request):
    if request.method == 'POST':
        old_pwd = request.POST['old_password']
        new_pwd = request.POST['new_password1']
        con_pwd = request.POST['new_password2']

        try:
            ex_user = AdminLogin.objects.get(password=old_pwd)

            if new_pwd == con_pwd:
                ex_user.password = new_pwd
                ex_user.save()
                messages.success(request, 'Password updated successfully. Please log in again.')
                return redirect('login')
            else:
                messages.error(request, 'New password and confirm password do not match.')
                return redirect('user_change_password')

        except AdminLogin.DoesNotExist:
            messages.error(request, 'Old password is incorrect.')
            return redirect('user_change_password')

    return render(request, 'change_password.html')



# department
def department(request):

     context = ({
     'department' : DepartmentDetails.objects.all()
     })
     return render(request,'add_department.html',context)

def insert_department(request):
     if request.method == 'POST':
          dname = request.POST['name']

          new_dept =  DepartmentDetails(department = dname)

          new_dept.save()

          return render(request,'add_department.html')



def edit_department(request, dept_id = 0):
     dept = DepartmentDetails.objects.get(dept_id = dept_id)
     context = ({
     'department' : dept
     })
     return render(request,'edit_department.html',context)

def update_department(request):
     if request.method == 'POST':
          dname = request.POST['name']
          status = request.POST['status']
          dept_id = request.POST['dept_id']

          ex_dept = DepartmentDetails.objects.get(dept_id = dept_id)

          ex_dept.department = dname
          ex_dept.department_status = status

          ex_dept.save()

          return render(request,'add_department.html')
     
def delete_dept(request, dept_id=0):
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        try:
            dept = DepartmentDetails.objects.get(dept_id=dept_id)
            dept.delete()
            return JsonResponse({'status': 'success', 'message': 'Department Deleted Successfully'})
        except DepartmentDetails.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Department not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


# user_details

def user_details(request):

     context = ({
     'users' : UserDetails.objects.all()
     })
     return render(request,'user_details.html',context)

def add_user(request):
     context = ({
         'department': DepartmentDetails.objects.all()
     })
    
     return render(request, 'add_user.html', context)


def insert_user(request):
    if request.method == 'POST':
        dept_id = request.POST.get('department')
        username = request.POST.get('username')
        ip_address = request.POST.get('ip_address')
        mobile = request.POST.get('mobile')
        system_name = request.POST.get('system_name')
        email_id = request.POST.get('email_id')

        # Optional: you can fetch department object if dept_id is given
        department = None
        if dept_id:
            try:
                department = DepartmentDetails.objects.get(dept_id=dept_id)
            except DepartmentDetails.DoesNotExist:
                department = None  # Or handle error appropriately

        # Save the user details
        new_user = UserDetails(
            dept=department,
            username=username,
            user_ip=ip_address,
            mobile=mobile,
            system_name=system_name,
            email_id=email_id,
            #user_create_id=request.user.id if request.user.is_authenticated else None
        )
        new_user.save()

        return render(request, 'add_user.html', {'success': True})

    departments = DepartmentDetails.objects.all()
    return render(request, 'add_user.html', {'department': departments})



def edit_user(request, user_id = 0):
     
    context = ({
         'department': DepartmentDetails.objects.all(),
         'user': UserDetails.objects.get(user_id = user_id)
     })
    return render(request,'edit_user.html',context)

def update_user(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        dept_id = request.POST['department']
        username = request.POST['username']
        ip_address = request.POST['ip_address']
        mobile = request.POST['mobile']
        system_name = request.POST['system_name']
        email_id = request.POST['email_id']

        ex_user = get_object_or_404(UserDetails, user_id=user_id)
        department = get_object_or_404(DepartmentDetails, dept_id=dept_id)

        ex_user.dept = department
        ex_user.username = username
        ex_user.user_ip = ip_address
        ex_user.mobile = mobile
        ex_user.system_name = system_name
        ex_user.email_id = email_id

        ex_user.save()

        return render(request, 'add_user.html', {'success': True})
    

def delete_user(request, user_id=0):
    user = get_object_or_404(UserDetails, user_id=user_id)
    user.delete()
    return redirect('user_details') 




def it_team_details(request):
    context = {
        'team': ITTeam.objects.all()
    }
    return render(request, 'it_team_details.html', context)


def add_it_team(request):
    context = ({
         'department': ITTeam.objects.all()
     })
    return render(request, 'add_it_team.html')


def insert_it_team(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        email_id = request.POST.get('email_id')
        status = request.POST.get('status')

        ITTeam.objects.create(
            name=name,
            username=username,
            password=password,
            mobile=mobile,
            email_id=email_id,
            status=status
        )
        return render(request, 'add_it_team.html', {'success': True})
    departments = DepartmentDetails.objects.all()

    return render(request, 'add_it_team.html')


def edit_it_team(request, it_team_id=0):
    team = get_object_or_404(ITTeam, it_team_id = it_team_id)
    return render(request, 'edit_it_team.html', {'team': team})


def update_it_team(request):
    if request.method == 'POST':
        team_id = request.POST['it_team_id']
        team = get_object_or_404(ITTeam, it_team_id=team_id)

        team.name = request.POST['name']
        team.username = request.POST['username']
        team.password = request.POST['password']
        team.mobile = request.POST['mobile']
        team.email_id = request.POST['email_id']
        team.status = request.POST['status']

        team.save()
        return render(request, 'add_it_team.html', {'success': True})
    
def delete_it_team(request, it_team_id=0):
    member = get_object_or_404(ITTeam, it_team_id=it_team_id)
    member.delete()
    return redirect('it_team_details')




# complain type

def add_complain_type(request):
    context = ({
         'complaints': ComplaintType.objects.all()
     })
    return render(request, 'add_complain_type.html', context)


def insert_complain_type(request):
     if request.method == 'POST':
          complain_type = request.POST['name']

          new_complain_type =  ComplaintType(complain = complain_type)

          new_complain_type.save()

          return redirect('add_complain_type')
     

def edit_complain_type(request, complain_type_id = 0):
     
    context = ({
         'complaints': ComplaintType.objects.get(complain_id = complain_type_id)
     })
    return render(request,'edit_complain_type.html',context)

def update_complain_type(request):
     if request.method == 'POST':
          complain_type = request.POST['name']
          status = request.POST['status']
          complain_type_id = request.POST['complain_id']

          ex_complain_type = ComplaintType.objects.get(complain_id = complain_type_id)

          ex_complain_type.complain = complain_type
          ex_complain_type.status = status

          ex_complain_type.save()

          return redirect('add_complain_type')

def delete_complain_type(request, complain_type_id=0):
    user = get_object_or_404(ComplaintType, complain_id=complain_type_id)
    user.delete()
    return redirect('add_complain_type') 




# complain desc


# List all complaint descriptions

# Add Complaint Description Page
def add_complaint_description(request):
    context   = ({
        'complaint_types': ComplaintType.objects.all(),
        'complaint_descriptions': ComplaintDescription.objects.select_related('complain_type')
    })
    return render(request, 'add-complaint-description.html', context)

# Insert Complaint Description to DB
def insert_complaint_description(request):
    if request.method == 'POST':
        complaint_type_id = request.POST['complain_type']
        description = request.POST['description']

        complaint_types = ComplaintType.objects.get(complain_id=complaint_type_id)

        new_complaint_description = ComplaintDescription(
            complain_type=complaint_types,
            description=description
        )
        new_complaint_description.save()

        return redirect('add_complaint_description')



# Edit Complaint Description Page
def edit_complaint_description(request, complain_desc_id=0):
    complaint_desc = ComplaintDescription.objects.get(complain_desc_id=complain_desc_id)
    context = {
        'comp_desc': complaint_desc,
        'complaint_types': ComplaintType.objects.all()
    }
    return render(request, 'edit_comp_desc.html', context)

# Update Complaint Description
def update_complaint_description(request):
    if request.method == 'POST':
        comp_desc_id = request.POST['comp_desc_id']
        complaint_types = request.POST.get('complain_type')  # or 'complain_desc_id' based on your form
        description = request.POST['description']
        status = request.POST['status']

        comp_desc = ComplaintDescription.objects.get(complain_desc_id=comp_desc_id)
        complaint_type = ComplaintType.objects.get(complain_id=complaint_types)

        comp_desc.complain_type = complaint_type
        comp_desc.description = description
        comp_desc.status = status

        comp_desc.save()

        return redirect('add_complaint_description')


# Delete Complaint Description
def delete_complaint_description(request, complain_desc_id=0):
    complaint_desc = get_object_or_404(ComplaintDescription, complain_desc_id=complain_desc_id)
    complaint_desc.delete()
    return redirect('add_complaint_description')



# user_details
def user_complain_details(request):
    context = {
        'complains': UserComplain.objects.all()
    }
    return render(request, 'user_complain.html', context)
def add_user_complain(request): 
    
    context = {
        'users': UserDetails.objects.all(),
        'departments': DepartmentDetails.objects.all(),
        'complain_types': ComplaintType.objects.all(),
        'complain_descs': ComplaintDescription.objects.all(),
        'it_teams': ITTeam.objects.all()
    }
    return render(request, 'add_new_complain.html', context)


def insert_user_complain(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        department_id = request.POST.get('department')
        complain_type_id = request.POST.get('complain_type')
        complain_desc_id = request.POST.get('complain_desc')
        it_team_id = request.POST.get('it_team')
        email_id = request.POST.get('email_id')
        complain_dt = request.POST.get('complain_dt')
        complain_time = request.POST.get('complain_time')
        status = request.POST.get('complain_status')

        UserComplain.objects.create(
            user_id=user_id,
            department_id=department_id,
            complain_type_id=complain_type_id,
            complain_desc_id=complain_desc_id,
            it_team_id=it_team_id,
            email_id=email_id,
            complain_dt=complain_dt or date.today(),
            complain_time=complain_time or datetime.now().time(),
            complain_status=status
        )
        return render(request, 'add_new_complain.html', {'success': True})

    return redirect('add_user_complain')


def edit_user_complain(request, user_complain_id=0):
    complain = get_object_or_404(UserComplain, user_complain_id=user_complain_id)
    context = {
        'complain': complain,
        'users': UserDetails.objects.all(),
        'departments': DepartmentDetails.objects.all(),
        'complain_types': ComplaintType.objects.all(),
        'complain_descs': ComplaintDescription.objects.all(),
        'it_teams': ITTeam.objects.all()
    }
    return render(request, 'edit_user_complain.html', context)


def update_user_complain(request):
    if request.method == 'POST':
        complain_id = request.POST.get('user_complain_id')
        complain = get_object_or_404(UserComplain, user_complain_id=complain_id)

        complain.user_id = request.POST.get('user')
        complain.department_id = request.POST.get('department')
        complain.complain_type_id = request.POST.get('complain_type')
        complain.complain_desc_id = request.POST.get('complain_desc')
        complain.it_team_id = request.POST.get('it_team')
        complain.email_id = request.POST.get('email_id')
        complain.complain_dt = request.POST.get('complain_dt')
        complain.complain_time = request.POST.get('complain_time')
        complain.complain_status = request.POST.get('complain_status')

        complain.save()
        return redirect('user_complain_details')


def delete_user_complain(request, user_complain_id=0):
    complain = get_object_or_404(UserComplain, user_complain_id=user_complain_id)
    complain.delete()
    return redirect('user_complain_details')


#complain_report
def complain_report(request):
    complaints = UserComplain.objects.all()
   

    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        # department_id = request.POST.get('department')
        # complaint_type_id = request.POST.get('complaint_type')
        # status = request.POST.get('status')

        if from_date and to_date:
            complaints = complaints.filter(complain_dt__range=[from_date, to_date])


            context = {
                'complaints': complaints,
            }
            return render(request, 'complain-report.html', context)
        
    return render(request, 'complain-report.html')


#change_password
def user_change_password(request):
    if request.method == 'POST':
        old = request.POST.get('old_password')
        new1 = request.POST.get('new_password1')
        new2 = request.POST.get('new_password2')

        user = request.user

        if not user.check_password(old):
            messages.error(request, 'Old password is incorrect.')
        elif new1 != new2:
            messages.error(request, 'New passwords do not match.')
        else:
            user.set_password(new1)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
            return redirect('user_change_password')

    return render(request, 'change_password.html')



#ajax fetch user
def fetch_user(request):
    if request.method == 'GET':
        department = request.GET.get('dept')

        # Fetch user associated with the department
        users = UserDetails.objects.filter(dept=department)

        # Prepare a list of tuples with (id, username)
        userdata = [(user.user_id, user.username) for user in users]

        # Return the data as JSON
        return JsonResponse(userdata, safe=False)


#fetch user image
def fetch_user_email(request):
    if request.method == 'GET':
        user = request.GET.get('user')

        # Fetch user associated with the department
        users = UserDetails.objects.get(user_id=user)

        # Prepare a list of tuples with (id, username)
        userdata = users.email_id

        # Return the data as JSON
        return JsonResponse(userdata, safe=False)

#fetch complain

def fetch_complain_desc_by_type(request):
    if request.method == 'GET':
        complain_type_id = request.GET.get('complain_type_id')
        descriptions = ComplaintDescription.objects.filter(complain_type_id=complain_type_id)

        # Return list of (id, description text)
        desc_data = [(desc.complain_desc_id, desc.description) for desc in descriptions]

        return JsonResponse(desc_data, safe=False)
    



def fetch_report(request):
     if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')

        
        Reports = UserComplain.objects.filter(from_date= from_date, to_date= to_date)

        context = {'complaint' : Reports}

        return render(request, 'complain-report.html',context)
     
     # ---- VIRTUAL ASSISTANT LOGIC ----


def virtual_assistant(request):
    user_msg = request.GET.get("msg", "").lower()

    responses = {
        "hi": "Hello! How can I assist you today?",
        "hello": "Hello! What IT problem are you facing?",
        "internet": "If your internet is slow, try restarting the router. If issue continues, create a complaint.",
        "system not starting": "Please check power cables. If still not working, raise a hardware complaint.",
        "software not working": "Try reinstalling the software. If issue persists, submit a complaint.",
        "how to raise complaint": "Go to: Complaint → Add Complaint → Fill details → Submit.",
        "track complaint": "Click on: Complaint → View Complaint Status.",
        "thank you": "You're welcome! Happy to help 😊"
    }

    # Fallback message
    reply = responses.get(user_msg, "Sorry, I didn't understand. You can raise a complaint for this issue.")

    return JsonResponse({"reply": reply})








