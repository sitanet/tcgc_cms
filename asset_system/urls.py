from django.urls import path
from . import views

urlpatterns = [
    path('asset_list/', views.asset_list, name='asset_list'),
    path('asset/<int:pk>/', views.asset_detail, name='asset_detail'),
    path('asset_create', views.asset_create, name='asset_create'),
    path('asset/<int:pk>/edit/', views.asset_edit, name='asset_edit'),
    path('asset/<int:pk>/delete/', views.asset_delete, name='asset_delete'),




    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('department_create', views.department_create, name='department_create'),
    path('departments/<int:pk>/edit/', views.department_edit, name='department_edit'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department_delete'),


    path('asset_class_create', views.asset_class_create, name='asset_class_create'),
    path('asset_classes/', views.asset_class_list, name='asset_class_list'),
    path('asset_classes/<int:pk>/', views.asset_class_detail, name='asset_class_detail'),
    path('asset_classes/<int:pk>/edit/', views.asset_class_edit, name='asset_class_edit'),
    path('asset_classes/<int:pk>/delete/', views.asset_class_delete, name='asset_class_delete'),
    path('asset_report_list', views.asset_report_list, name='asset_report_list'),
    path('asset_depreciation_report/', views.asset_depreciation_report, name='asset_depreciation_report'),


    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('category_create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),




    # Location URLs
    path('locations/', views.location_list, name='location_list'),
    path('locations/<int:pk>/', views.location_detail, name='location_detail'),
    path('locations/new/', views.location_create, name='location_create'),
    path('locations/<int:pk>/edit/', views.location_edit, name='location_edit'),
    path('locations/<int:pk>/delete/', views.location_delete, name='location_delete'),


    

    path('maintenance/create/', views.maintenance_record_create, name='maintenance_record_create'),
    path('maintenance/<int:pk>/', views.maintenance_record_detail, name='maintenance_record_detail'),
    path('maintenance/<int:pk>/edit/', views.maintenance_record_edit, name='maintenance_record_edit'),
    path('maintenance/<int:pk>/delete/', views.maintenance_record_delete, name='maintenance_record_delete'),
    path('maintenance/', views.maintenance_record_list, name='maintenance_record_list'),
]
