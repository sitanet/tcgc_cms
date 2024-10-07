from django.urls import path
from . import views




urlpatterns = [
    # path('cust_menu/', views.cust_menu, name='cust_menu'),
  
    path('coor_register_member/', views.coor_register_member, name='coor_register_member'),
    path('coor_display_all_member/', views.coor_display_all_member, name='coor_display_all_member'),
    path('coor_display_comment/', views.coor_display_comment, name='coor_display_comment'),
    path('coor_new_comment/<int:id>/', views.coor_new_comment, name='coor_new_comment'),
    path('my_team_member_list/', views.my_team_member_list, name='my_team_member_list'),
    path('my_team_member_comment/', views.my_team_member_comment, name='my_team_member_comment'),
    path('coor_member_detail/<int:id>/', views.coor_member_detail, name='coor_member_detail'),
    path('registration/', views.registration, name='registration'),
    
 
    
]