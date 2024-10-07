from django.urls import path
from . import views



urlpatterns = [
    path('team_dashboard/', views.team_dashboard, name='team_dashboard'),
    path('mis_dashboard/', views.mis_dashboard, name='mis_dashboard'),
    path('service_team_dashboard/', views.service_team_dashboard, name='service_team_dashboard'),
    path('myAccount/', views.myAccount, name='myAccount'),
    path('registeruser/', views.registeruser, name='registeruser'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('forget_success/', views.forget_success, name='forget_success'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('coor_dashboard/', views.coor_dashboard, name='coor_dashboard'),
    path('past_dashboard/', views.past_dashboard, name='past_dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('change_password/', views.change_password, name='change_password'),
    path('users/edit/<int:id>/', views.edit_user, name='edit_user'),

    path('kbn_career_dashboard/', views.kbn_career_dashboard, name='kbn_career_dashboard'),
    path('household_head_dashboard/', views.household_head_dashboard, name='household_head_dashboard'),


    path('active_member/', views.active_member, name='active_member'),
    path('member_inctive/', views.member_inctive, name='member_inctive'),
    path('member_male/', views.member_male, name='member_male'),
    path('member_female/', views.member_female, name='member_female'),
    path('member_single/', views.member_single, name='member_single'),
    path('member_married/', views.member_married, name='member_married'),
    path('facilitator/', views.facilitator, name='facilitator'),
    path('student/', views.student, name='student'),
    path('career/', views.career, name='career'),
    path('business/', views.business, name='business'),
    
    path('facilitator_dashboard/', views.facilitator_dashboard, name='facilitator_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('career_dashboard/', views.career_dashboard, name='career_dashboard'),
    path('business_dashboard/', views.business_dashboard, name='business_dashboard'),
 


    path('list_users/', views.list_users, name='list_users'),
    
    path('users/delete/<int:id>/', views.delete_user, name='delete_user'),
    
]
  