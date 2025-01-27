from django.urls import path
from . import views

urlpatterns = [
    path('files/', views.file_list, name='file_list_fbv'),
    path('files/create/', views.file_create, name='file_create_fbv'),
    path('files/<int:file_id>/', views.file_detail, name='file_detail_fbv'),
    path('files/<int:pk>/update/', views.file_update, name='file_update_fbv'),
    path('files/<int:pk>/delete/', views.file_delete, name='file_delete_fbv'),
]