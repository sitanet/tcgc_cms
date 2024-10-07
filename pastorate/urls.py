from django.urls import path
from . import views




urlpatterns = [
    # path('cust_menu/', views.cust_menu, name='cust_menu'),
  
    path('past_register_member/', views.past_register_member, name='past_register_member'),
    path('past_display_all_member/', views.past_display_all_member, name='past_display_all_member'),
    path('display_kbn_business/', views.display_kbn_business, name='display_kbn_business'),
    path('member_male/', views.member_male, name='member_male'),
    path('member_female/', views.member_female, name='member_female'),
    path('family/', views.family, name='family'),
    path('member_married/', views.member_married, name='member_married'),
    path('member_single/', views.member_single, name='member_single'),
    path('children/', views.children, name='children'),
    path('display_kbn_car/', views.display_kbn_car, name='display_kbn_car'),
    path('past_display_comment/', views.past_display_comment, name='past_display_comment'),
    path('past_new_comment/<int:id>/', views.past_new_comment, name='past_new_comment'),
    # path('my_team_member_list/', views.my_team_member_list, name='my_team_member_list'),
    # path('my_team_member_comment/', views.my_team_member_comment, name='my_team_member_comment'),
    path('past_member_detail/<int:id>/', views.past_member_detail, name='past_member_detail'),
    
 
    
]