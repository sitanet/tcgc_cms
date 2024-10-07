from datetime import datetime
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import message
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import urlsafe_base64_decode

from accounts.utils import detectUser, send_verification_email
from asset_system.models import Asset, Asset_Class
from follow_app.models import NYSC, Business, Career, Family, Household, Member


from .forms import PasswordChangeForm, UserEditForm, UserForm, UserProfileForm, UserProfilePictureForm
from .models import User, UserProfile
from django.contrib import messages, auth
# from .utils import detectUser, send_verification_email
from django.contrib.auth.decorators import login_required, user_passes_test

from django.core.exceptions import PermissionDenied
# from vendor.models import Vendor
# from django.template.defaultfilters import slugify
# from orders.models import Order
import datetime

# Create your views here.

# Restrict the vendor from accessing the customer page
def check_role_admin(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied


# Restrict the customer from accessing the vendor page
def check_role_coordinator(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied
    
def check_role_team_member(user):
    if user.role == 3:
        return True
    else:
        raise PermissionDenied
    

def check_role_pastorate(user):
    if user.role == 4:
        return True
    else:
        raise PermissionDenied

def check_role_facilitator(user):
    if user.role == 5:
        return True
    else:
        raise PermissionDenied
    
def check_role_student(user):
    if user.role == 6:
        return True
    else:
        raise PermissionDenied

def check_role_career(user):
    if user.role == 7:
        return True
    else:
        raise PermissionDenied
    
    
def check_role_business(user):
    if user.role == 8:
        return True
    else:
        raise PermissionDenied
    
def check_role_service_team(user):
    if user.role == 9:
        return True
    else:
        raise PermissionDenied
    


def check_role_mis(user):
    if user.role == 10:
        return True
    else:
        raise PermissionDenied
    

def check_role_household(user):
    if user.role == 11:
        return True
    else:
        raise PermissionDenied

def check_role_kbn_career(user):
    if user.role == 12:
        return True
    else:
        raise PermissionDenied
    
def check_role_kbn_business(user):
    if user.role == 13:
        return True
    else:
        raise PermissionDenied
    
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserForm
from .models import User
from .utils import send_verification_email  # Assuming you have this utility function
from django.conf import settings
import requests

@login_required(login_url='login')
@user_passes_test(check_role_admin)
# def registeruser(request):
     
#      if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
          
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
          
#             password = form.cleaned_data['password']
#             phone_number = form.cleaned_data['phone_number']
#             role = form.cleaned_data['role']

#             user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, role=role, phone_number=phone_number, password=password)
            
#             user.save()
#             messages.success(request, 'You have successfull register User')

#             # Send verification email
#             mail_subject = 'Please activate your account'
#             email_template = 'accounts/email/accounts_verification_email.html'
#             send_verification_email(request, user, mail_subject, email_template)
#             messages.success(request, 'Your account has been registered sucessfully!')
#             return redirect('registeruser')
#         else:
#             print('invalid form')
#             print(form.errors)
#      else:
#         form = UserForm()
#      context = {
#         'form': form,
#     }
#      return render(request, 'accounts/registeruser.html', context)




def registeruser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']
            role = form.cleaned_data['role']

            try:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    role=role,
                    phone_number=phone_number,
                    password=password
                )
                user.save()
                messages.success(request, 'You have successfully registered.')

                # Send verification email
                mail_subject = 'Please activate your account'
                email_template = 'accounts/email/accounts_verification_email.html'
                send_verification_email(request, user, mail_subject, email_template)
                messages.success(request, 'Your account has been registered successfully!')

                # Send SMS via Termii
                print(f'Sending SMS to {phone_number}...')
                sms_body = f"Hello {first_name}, your account has been registered successfully on TCGC MOS. Please check your email to activate!"
                termii_api_key = settings.TERMII_API_KEY
                termii_sender_id = settings.TERMII_SENDER_ID
                termii_url = 'https://api.ng.termii.com/api/sms/send'

                payload = {
                    "to": phone_number,
                    "from": termii_sender_id,
                    "sms": sms_body,
                    "type": "plain",
                    "channel": "dnd",
                    "api_key": termii_api_key
                }

                response = requests.post(termii_url, json=payload)
                response_data = response.json()
                if response.status_code == 200 and response_data.get('status') == 'success':
                    print('SMS sent successfully')
                else:
                    error_message = response_data.get('message', 'Failed to send SMS')
                    print(f'Error sending SMS: {error_message}')
                    messages.error(request, f'Failed to send SMS: {error_message}')

            except Exception as e:
                messages.error(request, f'Failed to register user: {e}')
                print(f'Error: {e}')
                return redirect('registeruser')

            return redirect('registeruser')
        else:
            print('Invalid form')
            print(form.errors)
    else:
        form = UserForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/registeruser.html', context)






 

@login_required(login_url='login')
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)

@login_required(login_url='login')
def dashboard(request):
    member = Member.objects.filter(status=1).count()
    member_inctive = Member.objects.filter(status=2).count()
    member_male = Member.objects.filter(gender=1).count()
    member_female = Member.objects.filter(gender=2).count()
    member_single = Member.objects.filter(marital_status=1).count()
    member_married = Member.objects.filter(marital_status=2).count()

    member_family = Family.objects.all().count()
    member_children = Member.objects.filter(marital_status=4).count()
    member_teenager = Member.objects.filter(marital_status=3).count()
  
    member_business = Business.objects.all().count()
    member_career = Career.objects.all().count()
    member_household = Household.objects.all().count()
    member_nysc = NYSC.objects.all().count()
    

    context = {
        'member': member,
        'member_inctive': member_inctive,
        'member_male': member_male,
        'member_female': member_female,
        'member_single': member_single,
        'member_married': member_married,
        
        'member_family':member_family,
        'member_children':member_children,
        'member_teenager':member_teenager,
        'member_business':member_business,
        'member_career':member_career,
        'member_household':member_household,
        'member_nysc':member_nysc,



    }
    return render(request, 'admin_staff/dashboard.html', context)




@login_required(login_url='login')
def mis_dashboard(request):
    member = Member.objects.filter(status=1).filter(team_lead=request.user.role).count()
    member_inctive = Member.objects.filter(status=2).filter(team_lead=request.user.role).count()
    member_male = Member.objects.filter(gender=1).filter(team_lead=request.user.role).count()
    member_female = Member.objects.filter(gender=2).filter(team_lead=request.user.role).count()
    member_single = Member.objects.filter(marital_status=1).filter(team_lead=request.user.role).count()
    member_family = Family.objects.all().count()
    member_children = Member.objects.filter(marital_status=4).filter(team_lead=request.user.role).count()
    member_teenager = Member.objects.filter(marital_status=3).count()
    member_married = Member.objects.filter(marital_status=2).filter(team_lead=request.user.role).count()
    member_business = Business.objects.all().count()
    member_career = Career.objects.all().count()
    

    context = {
        'member': member,
        'member_inctive': member_inctive,
        'member_male': member_male,
        'member_female': member_female,
        'member_single': member_single,
        'member_family': member_family,
        'member_children':member_children,
        'member_married':member_married,
        'member_business':member_business,
        'member_career':member_career,
        'member_teenager':member_teenager,
        
    }
    return render(request, 'mis/mis_dashboard.html', context)








@login_required(login_url='login')
def coor_dashboard(request):
    member = Member.objects.filter(status=1).filter(team_lead=request.user.username).count()
    member_inctive = Member.objects.filter(status=2).filter(team_lead=request.user.username).count()
    member_male = Member.objects.filter(gender=1).filter(team_lead=request.user.username).count()
    member_female = Member.objects.filter(gender=2).filter(team_lead=request.user.username).count()
    member_single = Member.objects.filter(marital_status=1).filter(team_lead=request.user.username).count()
    member_family = Family.objects.all().count()
    member_children = Member.objects.filter(marital_status=4).filter(team_lead=request.user.username).count()
    member_teenager = Member.objects.filter(marital_status=3).count()
    member_married = Member.objects.filter(marital_status=2).filter(team_lead=request.user.username).count()
    member_business = Business.objects.all().count()
    member_career = Career.objects.all().count()
    

    context = {
        'member': member,
        'member_inctive': member_inctive,
        'member_male': member_male,
        'member_female': member_female,
        'member_single': member_single,
        'member_family': member_family,
        'member_children':member_children,
        'member_married':member_married,
        'member_business':member_business,
        'member_career':member_career,
        'member_teenager':member_teenager,
        
    }
    return render(request, 'coordinators/coor_dashboard.html', context)









def household_head_dashboard(request):
    member = Member.objects.filter(status=1).filter(team_lead=request.user.username).count()
    member_inctive = Member.objects.filter(status=2).filter(team_lead=request.user.username).count()
    member_male = Member.objects.filter(gender=1).filter(team_lead=request.user.username).count()
    member_female = Member.objects.filter(gender=2).filter(team_lead=request.user.username).count()
    member_single = Member.objects.filter(marital_status=1).filter(team_lead=request.user.username).count()
    member_family = Family.objects.all().count()
    member_children = Member.objects.filter(marital_status=4).filter(team_lead=request.user.username).count()
    member_teenager = Member.objects.filter(marital_status=3).count()
    member_married = Member.objects.filter(marital_status=2).filter(team_lead=request.user.username).count()
    member_business = Business.objects.all().count()
    member_career = Career.objects.all().count()
    

    context = {
        'member': member,
        'member_inctive': member_inctive,
        'member_male': member_male,
        'member_female': member_female,
        'member_single': member_single,
        'member_family': member_family,
        'member_children':member_children,
        'member_married':member_married,
        'member_business':member_business,
        'member_career':member_career,
        'member_teenager':member_teenager,
        
    }
    return render(request, 'household_head/household_head_dashboard.html', context)


@login_required(login_url='login')
def past_dashboard(request):
    member = Member.objects.filter(status=1).count()
    member_inctive = Member.objects.filter(status=2).count()
    member_male = Member.objects.filter(gender=1).count()
    member_female = Member.objects.filter(gender=2).count()
    member_single = Member.objects.filter(marital_status=1).count()
    member_family = Family.objects.all().count()
    member_children = Member.objects.filter(marital_status=4).count()
    member_teenager = Member.objects.filter(marital_status=3).count()
    member_married = Member.objects.filter(marital_status=2).count()
    member_business = Business.objects.all().count()
    member_career = Career.objects.all().count()
    member_asset = Asset.objects.all().count()
    

    context = {
        'member': member,
        'member_inctive': member_inctive,
        'member_male': member_male,
        'member_female': member_female,
        'member_single': member_single,
        'member_married': member_married,
        'member_family':member_family,
        'member_children':member_children,
        'member_teenager':member_teenager,
        'member_business':member_business,
        'member_career':member_career,
        'member_asset':member_asset,

    }
    return render(request, 'pastorate/past_dashboard.html', context)


@login_required(login_url='login')
def team_dashboard(request):
    member = Member.objects.filter(status=1).filter(team_member=request.user).count()
    member_inctive = Member.objects.filter(status=2).filter(team_member=request.user).count()
    member_male = Member.objects.filter(gender=1).filter(team_member=request.user).count()
    member_female = Member.objects.filter(gender=2).filter(team_member=request.user).count()
    member_single = Member.objects.filter(marital_status=1).filter(team_member=request.user).count()
    member_married = Member.objects.filter(marital_status=2).filter(team_member=request.user).count()
    

    context = {
        'member': member,
        'member_inctive': member_inctive,
        'member_male': member_male,
        'member_female': member_female,
        'member_single': member_single,
        'member_married': member_married,
    }
    return render(request, 'team_members/team_dashboard.html', context)



@login_required(login_url='login')
def kbn_career_dashboard(request):
    return render(request, 'kbn_career/kbn_career_dashboard.html')


@login_required(login_url='login')
def kbn_business_dashboard(request):
    return render(request, 'kbn_business/kbn_business_dashboard.html')




from django.contrib.auth import update_session_auth_hash




@login_required
def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User profile was successfully updated!')
            return redirect('list_users')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'accounts/edit_user.html', {'form': form, 'user': user})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['new_password'])
            user.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(instance=request.user)
    return render(request, 'accounts/change_password.html', {'form': form})







from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def list_users(request):
    users = User.objects.all()
    return render(request, 'accounts/list_users.html', {'users': users})



@login_required
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User was successfully deleted!')
        return redirect('list_users')
    return render(request, 'confirm_delete.html', {'user': user})






def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('myAccount')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('myAccount')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logged in.')
    return redirect('login')



# def profile(request):
   
#     return render(request, 'accounts/profile.html')


# def profile(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # Redirect to the user's profile page
#     else:
#         form = UserForm(instance=request.user)
#     return render(request, 'accounts/profile.html', {'form': form})




def profile(request):
    if request.method == 'POST':
        form = UserProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated.')
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = UserProfilePictureForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})






def activate(request, uidb64, token):
    # Activate the user by setting the is_active status to True
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulation! Your account is activated.')
        return redirect('myAccount')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('myAccount')



def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)

            # send reset password email
            mail_subject = 'Reset Your Password'
            email_template = 'accounts/email/reset_password_email.html'
            send_verification_email(request, user, mail_subject, email_template)

            messages.success(request, 'Password reset link has been sent to your email address.')
            return redirect('forget_success')
        else:
            messages.error(request, 'Account does not exist')
            return redirect('forgot_password')
    return render(request, 'accounts/forgot_password.html')



def forget_success(request):
    return render(request, 'accounts/forget_success.html')





def reset_password_validate(request, uidb64, token):
    # validate the user by decoding the token and user pk
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request, 'Please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('myAccount')



def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('reset_password')
    return render(request, 'accounts/reset_password.html')


def change_password(request):
   
    return render(request, 'accounts/change_password.html')






def active_member(request):
    active_member = Member.objects.filter(status=1)
    context = {
        'active_member': active_member,
    }
    return render(request, 'admin_staff/active_member.html', context)

def member_inctive(request):
    member_inctive = Member.objects.filter(status=1)
    context = {
        'member_inctive': member_inctive,
    }
    return render(request, 'admin_staff/member_inctive.html', context)



def member_male(request):
    member_male = Member.objects.filter(gender=1)
    context = {
        'member_male': member_male,
    }
    return render(request, 'admin_staff/member_male.html', context)



def member_female(request):
    member_female = Member.objects.filter(gender=2)
    context = {
        'member_female': member_female,
    }
    return render(request, 'admin_staff/member_female.html', context)



    

def member_single(request):
    member_single = Member.objects.filter(marital_status=1)
    context = {
        'member_single': member_single,
    }
    return render(request, 'admin_staff/member_single.html', context)



def member_married(request):
    member_married = Member.objects.filter(marital_status=2)
    context = {
        'member_married': member_married,
    }
    return render(request, 'admin_staff/member_married.html', context)




def facilitator(request):
    member_married = Member.objects.filter(marital_status=2)
    context = {
        'member_married': member_married,
    }
    return render(request, 'admin_staff/dashboard.html', context)

def career(request):
    member_married = Member.objects.filter(marital_status=2)
    context = {
        'member_married': member_married,
    }
    return render(request, 'admin_staff/dashboard.html', context)

def student(request):
    member_married = Member.objects.filter(marital_status=2)
    context = {
        'member_married': member_married,
    }
    return render(request, 'admin_staff/dashboard.html', context)

def business(request):
    member_married = Member.objects.filter(marital_status=2)
    context = {
        'member_married': member_married,
    }
    return render(request, 'admin_staff/dashboard.html', context)


def facilitator_dashboard(request):
    return render(request, 'kbn/facilitator_dashboard.html')

def student_dashboard(request):
    return render(request, 'student/student_dashboard.html')


def career_dashboard(request):
    return render(request, 'career/career_dashboard.html')

def business_dashboard(request):
    return render(request, 'business/business_dashboard.html')

def service_team_dashboard(request):
    return render(request, 'Service_team/service_team_dashboard.html')