from django.urls import path
from . import views



urlpatterns = [
    # path('cust_menu/', views.cust_menu, name='cust_menu'),
    # path('profile/', views.profile, name='profile'),
    path('register_member/', views.register_member, name='register_member'),
    path('display_all_member/', views.display_all_member, name='display_all_member'),
    path('asset_management/', views.asset_management, name='asset_management'),
    
    path('display_kbn_business/', views.display_kbn_business, name='display_kbn_business'),
    path('display_kbn_car/', views.display_kbn_car, name='display_kbn_car'),
    
    path('member_detail_universal/<int:id>/', views.member_detail_universal, name='member_detail_universal'),
    path('member_male_detail/<int:id>/', views.member_male_detail, name='member_male_detail'),
    path('member_female_detail/<int:id>/', views.member_female_detail, name='member_female_detail'),

    path('family/<int:id>/', views.family_detail, name='family_detail'),
    path('families/<int:id>/delete/', views.delete_family, name='delete_family'),
    
    path('display_comment/', views.display_comment, name='display_comment'),
    path('all_comment/', views.all_comment, name='all_comment'),
    path('new_comment/<int:id>/', views.new_comment, name='new_comment'),
    path('member_detail/<int:id>/', views.member_detail, name='member_detail'),
    path('delete_member/<int:id>/', views.delete_member, name='delete_member'),
    path('add_coordinator/', views.add_coordinator, name='add_coordinator'),
    path('network_not_available/', views.network_not_available, name='network_not_available'),
    path('admin_registration/', views.admin_registration, name='admin_registration'),


    path('members/', views.list_members, name='list_members'),
    path('list_members_student/', views.list_members_student, name='list_members_student'),
    path('create-student/<int:member_id>/', views.create_student, name='create_student'),
    path('student-success/', views.success_page, name='student_success'),

    path('create_nysc/<int:member_id>/', views.create_nysc, name='create_nysc'),
    path('success/', views.success, name='success'),
    path('nysc/', views.nysc, name='nysc'),


    path('create_child/<int:member_id>/', views.create_child, name='create_child'),
    path('child_success/', views.child_success, name='child_success'),
    path('list_members_child/', views.list_members_child, name='list_members_child'),
    path('children_detail/<int:id>/', views.children_detail, name='children_detail'),


    path('list_members_nysc/', views.list_members_nysc, name='list_members_nysc'),

    path('nysc_detail/<int:id>/', views.nysc_detail, name='nysc_detail'),
    


    # path('create_kbn/<int:member_id>/', views.create_kbn, name='create_kbn'),
    path('kbn_success/', views.kbn_success, name='kbn_success'),
    path('list_members_bus_kbn/', views.list_members_bus_kbn, name='list_members_bus_kbn'),
    path('list_members_car_kbn/', views.list_members_car_kbn, name='list_members_car_kbn'),

    
    path('create-family/<int:member_id>/', views.create_family, name='create_family'),
    path('search-wife/', views.search_wife, name='search_wife'),
    path('list_family/', views.list_family, name='list_family'),


    path('kbn_bus_car/', views.kbn_bus_car, name='kbn_bus_car'),

    path('create_career_profile/<int:member_id>/', views.create_career_profile, name='create_career_profile'),
    path('create_business_profile/<int:member_id>/', views.create_business_profile, name='create_business_profile'),

    path('career_list/', views.career_list, name='career_list'),
    path('career_detail/<int:pk>/', views.career_detail, name='career_detail'),
    path('career/<int:pk>/delete/', views.career_delete, name='career_delete'),
    
    path('business_list/', views.business_list, name='business_list'),
    path('business_detail/<int:pk>/', views.business_detail, name='business_detail'),
    path('business/<int:pk>/delete/', views.business_delete, name='business_delete'),

    
    path('member_female/', views.member_female, name='member_female'),
    path('family/', views.family, name='family'),
    path('member_married/', views.member_married, name='member_married'),
    path('member_single/', views.member_single, name='member_single'),
    path('children/', views.children, name='children'),
    path('display_kbn_business_admin/', views.display_kbn_business_admin, name='display_kbn_business_admin'),
    path('display_kbn_car_admin/', views.display_kbn_car_admin, name='display_kbn_car_admin'),


    
    path('household_list/', views.household_list, name='household_list'),
    # path('households/add/', views.add_household, name='add_household'),
  

    


    path('create-household/', views.create_household, name='create_household'),
    path('search-members/', views.search_members, name='search_members'),

    # #Complain
    # path('file_complaint/', views.file_complaint, name='file_complaint'),
    path('households/add_member/<int:household_id>/', views.add_member, name='add_member'),
    path('chats/', views.list_chats, name='list_chats'),
    path('household/<int:household_id>/chat/', views.chat_messages, name='chat_messages'),
    # path('households/complaints/', views.households_with_complaints, name='households_with_complaints'),
    # path('households/<int:household_id>/complaints/', views.household_complaints, name='household_complaints'),
    # path('complaints/<int:complaint_id>/resolve/', views.mark_resolved, name='mark_resolved'),
   
    # path('create-tcgc-household/', views.create_tcgc_household, name='create_tcgc_household'),
    # path('search-members/', views.search_members, name='search_members'),
    path('members_by_household_username/<int:username_id>/', views.members_by_household_username, name='members_by_household_username'),
    path('past_members_by_household_username/<int:username_id>/', views.past_members_by_household_username, name='past_members_by_household_username'),
    
    path('query_member/<int:user_id>/', views.query_member, name='query_member'),
    path('household/<int:household_id>/', views.household_detail, name='household_detail'),
    # path('household/<int:household_id>/add_member/', views.add_member, name='add_member'),
    path('household/<int:household_member_id>/edit_member/', views.edit_member, name='edit_member'),
    path('household/<int:household_member_id>/delete_member/', views.delete_member, name='delete_member'),
    # path('search_member_add/', views.search_member_add, name='search_member_add'),


    path('household/members/', views.household_members_view, name='household_members_view'),  # URL to view household members
    path('household/members/send-query/<int:member_id>/', views.send_query_view, name='send_query'),  # URL to send a query

    path('teenager_member_list/', views.teenager_member_list, name='teenager_member_list'),
    path('admin_teenager_list/', views.admin_teenager_list, name='admin_teenager_list'),
    path('teenagers/', views.teenager_list, name='teenager_list'),
    path('teenagers/add/<int:member_id>/', views.add_teenager, name='add_teenager'),
    path('teenagers/edit/<int:teenager_id>/', views.edit_teenager, name='edit_teenager'),
    path('teenagers/delete/<int:teenager_id>/', views.delete_teenager, name='delete_teenager'),
    path('teenagers/<int:teenager_id>/', views.teenager_detail, name='teenager_detail'),
    path('business_detail_admin/<int:pk>/', views.business_detail_admin, name='business_detail_admin'),


    path('create_message/', views.create_message, name='create_message'),
    path('messages/', views.past_message_list, name='past_message_list'),
    path('house_message_list/', views.house_message_list, name='house_message_list'),
    path('message/<int:message_id>/', views.past_message_detail, name='past_message_detail'),
    # path('notifications/', views.notifications_view, name='notifications'),
    path('house_message_detail/<int:message_id>/', views.house_message_detail, name='house_message_detail'),
    path('messages/<int:message_id>/reply/', views.reply_message, name='reply_message'),


]