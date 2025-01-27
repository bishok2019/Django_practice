from django.shortcuts import render, redirect, get_object_or_404
from .models import UploadedFile
from .forms import UploadedFileForm

from logger import log_method_call
# create
def file_create(request):
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list_fbv')
    else:
        form = UploadedFileForm()
    return render(request, 'file_form.html', {'form': form})

# read (list)
@log_method_call
def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'file_list.html', {'files': files})

# read (detail)
def file_detail(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    return render(request, 'file_detail.html', {'files': file})

# update
def file_update(request, pk):
    file = get_object_or_404(UploadedFile, pk=pk)
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            return redirect('file_list_fbv')
    else:
        form = UploadedFileForm(instance=file)
    return render(request, 'file_form.html', {'form': form})

# delete
def file_delete(request, pk):
    file = get_object_or_404(UploadedFile, pk=pk)
    if request.method == 'POST':
        file.delete()
        return redirect('file_list_fbv')
    return render(request, 'file_confirm_delete.html', {'file': file})