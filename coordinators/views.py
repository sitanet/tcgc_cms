from tokenize import Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import User

from accounts.views import check_role_admin, check_role_coordinator
from follow_app.forms import CommentForm, MemberForm
from django.contrib import messages

from follow_app.models import Team_Lead, Member, TeamMember
from follow_app.models import Comment
from django.template.loader import render_to_string
from django.core.mail import send_mail


# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

from follow_app.forms import MemberForm
from follow_app.models import Team_Lead, TeamMember, User
from django.conf import settings
from follow_app.utils import send_sms




from .utils import send_whatsapp
from .sms_service import send_sms  # Import the send_sms function

@user_passes_test(check_role_coordinator)

def coor_register_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the member instance
            member = form.save(commit=False)
            member.user = request.user
            member.save()

            # Log member registration details
            print(f"Member {member.first_name} has been registered with phone number {member.phone_no}.")

            recipient_name = member.first_name
            phone_number = member.phone_no

            # Send SMS to the new member using Termii
            try:
                sms_body = f"Hello {recipient_name}, welcome to The CityGate Church! We're thrilled to have you with us. Stay Blessed."
                print(f"Sending SMS to {phone_number} with message: {sms_body}")
                
                # Send the SMS and capture the response
                sms_response = send_sms(phone_number, sms_body, bypass_dnd=True)

                # Print the entire SMS API response
                print(f'SMS API Response: {sms_response}')

                # Check if the SMS was successfully sent
                if 'error' not in sms_response and sms_response.get('status') == 'success':
                    messages.success(request, 'Account has been registered successfully! SMS sent to the member.')
                    print(f"SMS successfully sent to {phone_number}.")
                else:
                    # Log the failure response
                    error_message = sms_response.get('error', f"Failed to send SMS. Response: {sms_response}")
                    messages.warning(request, f"Account registered, but failed to send SMS.")
                    print(f"Error sending SMS to {phone_number}: {error_message}")
            except Exception as e:
                error_message = f'Failed to send SMS: {e}'
                messages.error(request, error_message)
                print(f"Exception occurred while sending SMS: {error_message}")

            # Redirect after successful registration
            return redirect('coor_display_all_member')
        else:
            # Log form validation errors
            print(f"Form errors: {form.errors}")
            messages.warning(request, form.errors)
            messages.warning(request, 'Please check the form fields and fill them correctly before submission!')
            return redirect('coor_register_member')
    else:
        # Initial form rendering
        form = MemberForm()
        team_lead = Team_Lead.objects.all()
        team_members = TeamMember.objects.all()
        member = User.objects.all()

        context = {
            'form': form,
            'team_lead': team_lead,
            'team_members': team_members,
            'member': member,
        }

    return render(request, 'coordinators/coor_register_member.html', context)


from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from follow_app.forms import MemberForm
from follow_app.models import Member, Team_Lead, TeamMember

@user_passes_test(check_role_coordinator)
def coor_member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    team_leads = None
    team_members = None

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been updated successfully!')
            return redirect('coor_display_all_member')
    else:
        form = MemberForm(instance=member)
        current_user = request.user
        team_leads = Team_Lead.objects.filter(name=current_user)
        team_members = TeamMember.objects.all()
    
    return render(request, 'coordinators/coor_member_detail.html', {
        'form': form,
        'member': member,
        'team_leads': team_leads,  # Changed from 'team_lead'
        'team_members': team_members
    })



@user_passes_test(check_role_coordinator)
def coor_display_comment(request):
    current_user = request.user
    comment = Comment.objects.filter(coor_comm=current_user)
    mem_com = Member.objects.all()
    context = {
         'comment':comment,
         'mem_com':mem_com,
         
     } 
    return render(request, 'coordinators/coor_display_comment.html', context)

@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def coor_display_all_member(request):
    current_user = request.user
    members = Member.objects.filter(user=current_user, status='1')
    return render(request, 'coordinators/coor_display_all_member.html', {'members': members})



# @login_required(login_url='login')
# def coor_display_comment(request):
#     return render(request, 'coordinators/display_comment.html')


@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def coor_new_comment(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.member = member
            comment.team_sup = request.user
            # comment.phone_number = UserProfile.phone_number
            comment.save()
            return redirect('coor_display_comment')
   
    else:
        form = CommentForm()
    context = {
         'member':member,
         'form':form,   
     }
    return render(request, 'coordinators/coor_new_comment.html', context)




@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def my_team_member_list(request):
    current_user = request.user
    member = Member.objects.filter(team_lead=current_user)
    context = {
         'member':member,
     } 
    return render(request, 'coordinators/my_team_member_list.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def my_team_member_comment(request):
    current_user = request.user
    member = Comment.objects.filter(coor_comm=current_user)
    context = {
         'member':member,
     } 
    return render(request, 'coordinators/my_team_member_comment.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_coordinator)

def registration(request):
 
    return render(request, 'coordinators/registration.html')