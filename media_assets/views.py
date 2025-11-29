from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from . models import MediaAsset 
from . forms import MediaAssetForm
# Create your views here.
'''
1. Dashboard view : this allows my user to uploaded items as public
2. My media view : this allows my user to view all their uploaded items
3.Upload media view : this allows my user to upload new media items
4.Edit media view : this allows my user to edit their uploaded media items
5.Delete media view : this allows my user to delete their uploaded media items
6.Media detail view : this allows my user to view details of a specific media item
'''
@login_required
def dashboard_view(request):
    '''main dashboard : show public media assets
    
    '''
    #capture alla ssets
    media_list = MediaAsset.objects.filter(is_public=True)
    #power search functionality
    query = request.GET.get('q')
    if query:
        media_list = media_list.filter(
            Q(title__icontains=query) |Q(description__icontains=query) |
            Q(uploaded_by__username__icontains=query)
        ).distinct() # to avoid duplicate records
        # contains pageination functionality
    paginator = Paginator(media_list, 12) # show 10 media assets per page
    media_assets = paginator.get_page(request.GET.get('page'))

    return render(request, 'media_assets/dashboard.html',{
        'media_assets': media_assets,
        'query': query
    })
@login_required
def my_media_view(request):
    ''' view to show all media assets uploaded by the logged in user
    '''
    media_list = MediaAsset.objects.filter(uploaded_by=request.user)
    # contains pageination functionality
    paginator = Paginator(media_list, 12) # show 12 media assets per page
    page_number = request.GET.get('page')
    media_assets = paginator.get_page(request.GET.get('page'))

    return render(request, 'media_assets/my_media.html',{
        'media_assets': media_assets
    })
@login_required
def upload_media_view(request):
    ''' view to handle media asset upload by logged in user
    '''
    if request.method == 'POST':
        form = MediaAssetForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.uploaded_by = request.user
            media.save()
            messages.success(request, 'Media asset uploaded successfully!')
            return redirect('media_assets:my_media')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MediaAssetForm()
    return render(request, 'media_assets/upload_media.html',{
        'form': form
    })

@login_required
def media_detail_view(request, pk):
    ''' view to show details of a specific media asset
    '''
    media = get_object_or_404(MediaAsset, pk=pk)
    # increment views count
    media.views_count += 1 
    media.save(update_fields=['views_count'])
    if not media.is_public and media.uploaded_by != request.user and not request.user.is_teacher() and not request.user.is_superuser:
        messages.error(request, 'You do not have permission to view this media asset.')
        return redirect('media_assets:dashboard')

    media.views_count += 1 
    media.save(update_fields=['views_count'])

    return render(request, 'media_assets/media_detail.html',{
        'media': media
    })

### edit and delete views to be added here later ###
@login_required
def edit_media_view(request, pk):
    ''' view to handle editing of a media asset by its owner
    '''
    media = get_object_or_404(MediaAsset, pk=pk)
    if not media.can_edit(request.user):
        messages.error(request, 'You can not edit this file.')
        return redirect('media_assets:dashboard')

    if request.method == 'POST':
        form = MediaAssetForm(request.POST, request.FILES, instance=media)
        if form.is_valid():
            form.save()
            messages.success(request, 'Media asset updated successfully!')
            return redirect('media_assets:media_detail', pk=pk)
          
    else:
        form = MediaAssetForm(instance=media)

    return render(request, 'media_assets/edit_media.html',{
        'form': form,
        'media': media
    })

@login_required
def delete_media_view(request, pk):
    ''' view to handle deletion of a media asset by its owner
    '''
    media = get_object_or_404(MediaAsset, pk=pk)
    if not media.can_edit(request.user):
        messages.error(request, 'You can not delete this file.')
        return redirect('media_assets:dashboard')

    if request.method == 'POST':
        media.delete()
        messages.success(request, 'Media asset deleted successfully!')
        return redirect('media_assets:my_media')

    return render(request, 'media_assets/delete_media.html',{
        'media': media
    })




