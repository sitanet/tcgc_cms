from django.shortcuts import render, redirect

from accounts.views import check_role_admin, check_role_business, check_role_career, check_role_facilitator, check_role_kbn_career, check_role_student
from .forms import DocumentForm
from .models import Document
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required(login_url='login')
@user_passes_test(check_role_facilitator)
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'kbn/upload_file.html', {
        'form': form
    })


@login_required(login_url='login')
@user_passes_test(check_role_facilitator)

def document_list(request):
    query = request.GET.get('q')
    if query:
        documents = Document.objects.filter(title__icontains=query)
    else:
        documents = Document.objects.all()
    return render(request, 'kbn/document_list.html', {'documents': documents})




@login_required(login_url='login')
@user_passes_test(check_role_kbn_career)

def career_document_list(request):
    query = request.GET.get('q')
    if query:
        documents = Document.objects.filter(title__icontains=query)
    else:
        documents = Document.objects.all()
    return render(request, 'kbn_career/career_document_list.html', {'documents': documents})


from django.shortcuts import render, get_object_or_404, redirect


def list_document(request):
    documents = Document.objects.all()
    return render(request, 'kbn/list_document.html', {'documents': documents})

def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'kbn/delete_document.html', {'document': document})





# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import YouTubeVideo

def list_youtube_video(request):
    videos = YouTubeVideo.objects.all()
    return render(request, 'kbn/list_youtube_video.html', {'videos': videos})

def delete_video(request, pk):
    video = get_object_or_404(YouTubeVideo, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('youtube_video_list')
    return render(request, 'delete_video.html', {'video': video})


@login_required(login_url='login')
@user_passes_test(check_role_facilitator)
def kbn_registration(request):
    return render(request, 'kbn/kbn_registration.html')


@login_required(login_url='login')
@user_passes_test(check_role_facilitator)
def material(request):
    return render(request, 'kbn/material.html')


# views.py
from django.shortcuts import render, redirect
from .models import YouTubeVideo
from .forms import YouTubeVideoForm


@login_required(login_url='login')
@user_passes_test(check_role_facilitator)
def upload_video(request):
    if request.method == 'POST':
        form = YouTubeVideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = YouTubeVideoForm()
    return render(request, 'kbn/upload_video.html', {'form': form})

from django.core.paginator import Paginator

@login_required(login_url='login')
@user_passes_test(check_role_facilitator)
def video_list(request):
    query = request.GET.get('q')
    if query:
        videos = YouTubeVideo.objects.filter(title__icontains=query)
    else:
        videos = YouTubeVideo.objects.all()
    
    paginator = Paginator(videos, 8)  # Show 8 videos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'kbn/video_list.html', {'page_obj': page_obj})


@login_required(login_url='login')
@user_passes_test(check_role_student)
def student_video_list(request):
    query = request.GET.get('q')
    if query:
        videos = YouTubeVideo.objects.filter(title__icontains=query)
    else:
        videos = YouTubeVideo.objects.all()
    
    paginator = Paginator(videos, 8)  # Show 8 videos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'student/video_list.html', {'page_obj': page_obj})




@login_required(login_url='login')
@user_passes_test(check_role_student)
def student_material(request):
    return render(request, 'student/material.html')





@login_required(login_url='login')
@user_passes_test(check_role_student)

def student_document_list(request):
    query = request.GET.get('q')
    if query:
        documents = Document.objects.filter(title__icontains=query, category='ST')
    else:
        documents = Document.objects.filter(category='ST')
    return render(request, 'student/document_list.html', {'documents': documents})







@login_required(login_url='login')
@user_passes_test(check_role_student)
def student_video_list(request):
    query = request.GET.get('q')
    if query:
        videos = YouTubeVideo.objects.filter(title__icontains=query)
    else:
        videos = YouTubeVideo.objects.all()
    
    paginator = Paginator(videos, 8)  # Show 8 videos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'student/video_list.html', {'page_obj': page_obj})




@login_required(login_url='login')
@user_passes_test(check_role_kbn_career)
def career_material(request):
    return render(request, 'career/material.html')




# @login_required(login_url='login')
# @user_passes_test(check_role_career)

# def career_document_list(request):
#     query = request.GET.get('q')
#     if query:
#         documents = Document.objects.filter(title__icontains=query, category='CA')
#     else:
#         documents = Document.objects.filter(category='CA')
#     return render(request, 'career/document_list.html', {'documents': documents})




@login_required(login_url='login')
@user_passes_test(check_role_kbn_career)
def career_video_list(request):
    query = request.GET.get('q')
    if query:
        videos = YouTubeVideo.objects.filter(title__icontains=query, category='CA')
    else:
        videos = YouTubeVideo.objects.filter(category='CA')
    
    paginator = Paginator(videos, 8)  # Show 8 videos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'career/video_list.html', {'page_obj': page_obj})







#business
@login_required(login_url='login')
@user_passes_test(check_role_business)
def business_material(request):
    return render(request, 'business/material.html')




@login_required(login_url='login')
@user_passes_test(check_role_business)

def business_document_list(request):
    query = request.GET.get('q')
    if query:
        documents = Document.objects.filter(title__icontains=query, category='BU')
    else:
        documents = Document.objects.filter(category='BU')
    return render(request, 'business/document_list.html', {'documents': documents})




@login_required(login_url='login')
@user_passes_test(check_role_business)
def business_video_list(request):
    query = request.GET.get('q')
    if query:
        videos = YouTubeVideo.objects.filter(title__icontains=query, category='BU')
    else:
        videos = YouTubeVideo.objects.filter(category='BU')
    
    paginator = Paginator(videos, 8)  # Show 8 videos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'business/video_list.html', {'page_obj': page_obj})
