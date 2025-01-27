# views.py
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import UploadedFile
from .forms import UploadedFileForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

####################################-View-####################################
from django.shortcuts import render, redirect
from django.views import View

class CustomMessageMixin:
    messages = 'Hello'

    def get_context_data(self, **kwargs):
        context = kwargs
        if self.messages:
            messages.info(self.request, self.messages)
        return context
    # def get_context_data(self, **kwargs):
    #     context = kwargs or{}
    #     if self.messages:
    #         messages.info(self.request, self.messages)
    #     return context
    
    # def dispatch(self, request, *args, **kwargs):
    #     if self.messages:
    #         messages.info(request, self.messages)
    #     return super().dispatch(request, *args, **kwargs)
    
class FileView(CustomMessageMixin,LoginRequiredMixin,View):
    template_name = 'file_list.html'
    login_url = 'login'
    messages = 'Welcome to file view'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request):
        files = UploadedFile.objects.all()
        form = UploadedFileForm()
        context = self.get_context_data()
        context.update({'files': files, 'form': form})
        return render(request, self.template_name, context)
        # return render(request, self.template_name, context,{'files': files, 'form': form}) # render doesnot work for more than 3 arguments
    
    def post(self, request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list_view')
        else:
            files = UploadedFile.objects.all()
        return render(request, self.template_name, {'files': files,'form': form})
        
class UploadFile(View):
    template_name = 'file_list.html'
    def get(self, request):
        files = UploadedFile.objects.all()
        form = UploadedFileForm()
        return render(request, self.template_name, {'files': files, 'form': form})
    def post(self, request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('file_list_view')
        else:
            return HttpResponse("invalid form submission")
        
class DeleteFile(View):

    template_name = 'file_confirm_delete.html'
    
    def get(self, request,pk):
        if UploadedFile.objects.filter(pk=pk).exists():
            files = UploadedFile.objects.get(pk=pk)
            form = UploadedFileForm()
            return render(request, self.template_name, {'file': files, 'form': form})
        messages.error(request, 'File not found')
        return redirect('file_list_view')

    # def post(self, request, pk):
    #     try:
    #         delete_file = UploadedFile.objects.get(pk=pk)
    #         delete_file.delete()
    #         messages.success(request, 'File deleted!')
    #         return redirect('file_list_view')
    #     except UploadedFile.DoesNotExist:
    #         messages.error(request, 'File not found')
    #         return redirect('file_list_view')

    def post(self, request, pk):
        if UploadedFile.objects.filter(pk=pk).exists():
            file_to_delete = UploadedFile.objects.get(pk=pk)
            file_to_delete.delete()
            messages.success(request, 'File deleted!')
            return redirect('file_list_view')

        # else:
        #     messages.error(request, 'File not found')
        #     return redirect('file_list_view', messages)

class ModifyFile(View):
    template_name = 'file_form.html'
    def get(self, request,pk):
        if UploadedFile.objects.filter(pk=pk).exists():
            files = UploadedFile.objects.get(pk=pk)
            print(f"Fetching  file for update: {files.title} (ID: {files.pk})")  # Debugging

            form = UploadedFileForm(instance=files)
            return render(request, self.template_name, {'file': files, 'form': form})
        messages.error(request, 'File not found')
        return redirect('file_list_view')
    
    def post(self, request, pk):
        if UploadedFile.objects.filter(pk=pk).exists():
            files = UploadedFile.objects.get(pk=pk)
            print(f"Updating file: {files.title} (ID: {files.pk})")  # Debugging

            form = UploadedFileForm(request.POST, request.FILES, instance=files)
            if form.is_valid():
                form.save()
                messages.success(request, 'File updated successfully!')
                return redirect('file_list_view')
            else:
                return render(request, 'file_form.html', {'files':files,'form': form})

        
####################################-GenericView-####################################
class FileListView(CustomMessageMixin,ListView):
    model = UploadedFile
    template_name = 'file_list.html'
    context_object_name = 'files'
    messages = 'welcome welcome'

class FileDetailView(DetailView):
    model = UploadedFile
    template_name = 'file_detail.html'
    context_object_name = 'files'

class FileCreateView(CreateView):
    model = UploadedFile
    form_class = UploadedFileForm
    template_name = 'file_form.html'
    success_url = reverse_lazy('file_list_cbv')

class FileUpdateView(UpdateView):
    model = UploadedFile
    form_class = UploadedFileForm
    template_name = 'file_form.html'
    success_url = reverse_lazy('file_list_cbv')

class FileDeleteView(DeleteView):
    model = UploadedFile
    template_name = 'file_confirm_delete.html'
    success_url = reverse_lazy('file_list_cbv')