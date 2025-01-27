# urls.py
from django.urls import path
# from . import views
from .views import ModifyFile,DeleteFile,UploadFile,FileView,FileListView, FileDetailView, FileCreateView, FileUpdateView, FileDeleteView

urlpatterns = [
    ####################################-View-####################################

    path('fileview/', FileView.as_view(), name='file_list_view'),
    path('upload/', UploadFile.as_view(), name='upload_file_view'),
    path('delete/<int:pk>/', DeleteFile.as_view(), name='delete_file_view'),
    path('modify/<int:pk>/', ModifyFile.as_view(), name='modify_file_view'),

    ####################################-GenericView-####################################
    path('files/', FileListView.as_view(), name='file_list_cbv'),
    path('files/create/', FileCreateView.as_view(), name='file_create_cbv'),
    path('files/<int:pk>/', FileDetailView.as_view(), name='file_detail_cbv'),
    path('files/<int:pk>/update/', FileUpdateView.as_view(), name='file_update_cbv'),
    path('files/<int:pk>/delete/', FileDeleteView.as_view(), name='file_delete_cbv'),
]