from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from admin_support.models import DepartmentDetails,ITTeam,ComplaintType,UserComplain,UserDetails,ComplaintDescription
from django.contrib import messages
from django.utils import timezone
# Create your views here.
def index(request):
    return render('index.html')




# def SignupPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         admin_name = request.POST.get('admin_name')
#         mobile = request.POST.get('mobile')
#         pass1 = request.POST.get('password1')
#         pass2 = request.POST.get('password2')

#         if pass1 != pass2:
#             return HttpResponse("Passwords do not match")

#         if ITTeam.objects.filter(username=username).exists():
#             return HttpResponse("Username already exists")
#         if ITTeam.objects.filter(email_id=email).exists():
#             return HttpResponse("Email already registered")

#         # hashed_password = make_password(pass1)
#         new_IT = ITTeam.objects.create(
#             username=username,
#             email_id=email,
#             password=pass1,
#             mobile=mobile,
#             # status='Active'
#         )
#         new_IT.save()
#         return redirect('login')  # Redirect to login page after successful signup

#     return render(request, 'signup.html')

def user_complain_it(request):
    it_id = request.session.get('IT_id')

    if not it_id:
        return redirect('IT/login')  # Redirect if session expired or not logged in

    complaints = UserComplain.objects.filter(it_team=it_id)

    context = {
        'complains': complaints
    }
    return render(request, 'User_complain_it.html', context)

# Login
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        try:
            admin = ITTeam.objects.get(username=username, status='Active')
            if (password == admin.password):
                request.session['IT_id'] = admin.it_team_id
                request.session['IT_name'] = admin.name
                return redirect('IT/user_complain')  # Redirect to your dashboard
            else:
                return HttpResponse("Incorrect password!")
        except ITTeam.DoesNotExist:
            return HttpResponse("IT Team does not exist or is inactive!")

    return render(request, 'login_IT.html')


# Logout
def LogoutPage(request):
    request.session.flush()  # Clear all session data
    return redirect('IT/login')
# Replace 'login' with your desired redirect target





def change_password_it(request):
    
    return render(request, 'Change_password_it.html')



def update_password(request):
    if request.method == 'POST':
        old_pwd = request.POST['old_password']
        new_pwd = request.POST['new_password1']
        con_pwd = request.POST['new_password2']

        # ✅ Get current IT user from session
        it_id = request.session.get('IT_id')
        if not it_id:
            messages.error(request, 'You must be logged in to change your password.')
            return redirect('IT/login')

        try:
            # ✅ Get the logged-in user
            ex_user = ITTeam.objects.get(it_team_id=it_id)

            # ✅ Check if old password matches
            if old_pwd != ex_user.password:
                messages.error(request, 'Old password is incorrect.')
                return redirect('IT/change_password_it')

            # ✅ Check if new password matches confirm
            if new_pwd != con_pwd:
                messages.error(request, 'New password and confirm password do not match.')
                return redirect('IT/change_password_it')

            # ✅ Save new password
            ex_user.password = new_pwd
            ex_user.save()

            messages.success(request, 'Password updated successfully. Please log in again.')
            return redirect('IT/login')

        except ITTeam.DoesNotExist:
            messages.error(request, 'User not found.')
            return redirect('IT/change_password_it')

    return render(request, 'change_password_it.html')




def edit_profile(request):
    it_id = request.session.get('IT_id')
    if not it_id:
        messages.error(request, "You must be logged in to access this page.")
        return redirect('IT/login')  # Correct redirection if session is missing

    try:
        it_user = ITTeam.objects.get(pk=it_id)  # Safely fetch logged-in IT user
    except ITTeam.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('IT/login')  # Redirect if user not found

    if request.method == 'POST':
        # Extract and update fields from POST data
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('phone')

        it_user.name = name
        it_user.username = username
        it_user.email_id = email
        it_user.mobile = mobile
        it_user.save()

        messages.success(request, "Profile updated successfully.")
        return redirect('IT/edit_profile')  # Refresh same page with success message

    return render(request, 'edit_profile.html', {'it_user': it_user})  # Render with current data

def update_user_complain(request, user_complain_id=0):
    if request.method == 'GET':
        try:
            complaint = UserComplain.objects.get(user_complain_id=user_complain_id)
            complaint.complain_status = 'Resolved'
            complaint.resolve_dt = timezone.now().date()
            complaint.resolve_time = timezone.now().time()
            complaint.save()
            messages.success(request, 'Complaint marked as resolved.')
        except UserComplain.DoesNotExist:
            messages.error(request, 'Complaint not found.')

        return redirect('IT/user_complain')  # Replace with your actual URL name

    messages.error(request, 'Invalid request.')
    return redirect('IT/user_complain')