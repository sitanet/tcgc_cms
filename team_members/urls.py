from django.urls import path
from . import views



urlpatterns = [
    # path('cust_menu/', views.cust_menu, name='cust_menu'),
    # path('team_dashboard/', views.team_dashboard, name='team_dashboard'),
    # path('team_register_member/', views.team_register_member, name='team_register_member'),
    path('team_display_all_member/', views.team_display_all_member, name='team_display_all_member'),
    path('team_display_comment/', views.team_display_comment, name='team_display_comment'),
    path('team_new_comment/<int:id>/', views.team_new_comment, name='team_new_comment'),
    # path('team_member_detail/', views.team_member_detail, name='team_member_detail'),
    # path('team_new_comment/', views.team_new_comment, name='team_new_comment'),

    
 
    
]