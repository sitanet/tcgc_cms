from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import User, UserProfile

from accounts.views import check_role_team_member
from follow_app.forms import CommentForm, MemberForm
from django.contrib import messages

from follow_app.models import Team_Lead, Member, TeamMember
from follow_app.models import Comment
from django.db.models import Q


# Create your views here.






@user_passes_test(check_role_team_member)
def team_display_comment(request):
    current_user = request.user
    mem_com = Member.objects.all()
    # user_profile = UserProfile.objects.get(user=current_user)
    # comment = Comment.objects.filter(Q(team_sup=current_user) & Q(coor_comm=user_profile))
    comment = Comment.objects.filter(team_mem=current_user)
  
    
    context = {
         'mem_com':mem_com,
         'comment':comment,
         
         
     } 
    return render(request, 'team_members/team_display_comment.html', context)

@login_required(login_url='login')
@user_passes_test(check_role_team_member)
def team_display_all_member(request):
    current_user = request.user
    member = Member.objects.filter(team_member=current_user).filter(status='1')

    return render(request, 'team_members/team_display_all_member.html', {'member': member})

# @login_required(login_url='login')
# def coor_display_comment(request):
#     return render(request, 'coordinators/display_comment.html')



@login_required(login_url='login')
@user_passes_test(check_role_team_member)
def team_new_comment(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.member = member
            comment.team_sup = request.user
            # comment.phone_number = UserProfile.phone_number
            comment.save()
            return redirect('team_display_comment')
   
    else:
        form = CommentForm()
    context = {
         'member':member,
         'form':form,   
     }
    return render(request, 'team_members/team_new_comment.html', context)








