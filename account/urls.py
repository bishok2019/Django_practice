from django.urls import path, include
from . import views
urlpatterns = [
    path('profile/', views.ProfileTemplateView.as_view(), name='profile-view'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('me/', views.RedirectUser.as_view(), name='index-to-profile'),

    # path('accounts/', include('django.contrib.auth.urls')),

]