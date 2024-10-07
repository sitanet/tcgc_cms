from django.urls import path
from . import views




urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('', views.document_list, name='document_list'),
   
    path('kbn_registration/', views.kbn_registration, name='kbn_registration'),
    path('material/', views.material, name='material'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('videos/', views.video_list, name='video_list'),
    path('student_video_list/', views.student_video_list, name='student_video_list'),
    path('student_material/', views.student_material, name='student_material'),
    path('student_document_list/', views.student_document_list, name='student_document_list'),
    path('career_material/', views.career_material, name='career_material'),
    path('career_document_list/', views.career_document_list, name='career_document_list'),
    path('career_video_list/', views.career_video_list, name='career_video_list'),

    path('business_material/', views.business_material, name='business_material'),
    path('business_document_list/', views.business_document_list, name='business_document_list'),
    path('business_video_list/', views.business_video_list, name='business_video_list'),

    path('documents/', views.list_document, name='list_document'),
    path('documents/delete/<int:pk>/', views.delete_document, name='delete_document'),

    
    path('youtube_videos/', views.list_youtube_video, name='list_youtube_video'),
    path('youtube_videos/delete/<int:pk>/', views.delete_video, name='delete_video'),
 
    
]

