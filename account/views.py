# views.py
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import LoginForm, SignupForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class LogOut(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logout Successfull')
        return redirect('login') 
    
class LoginView(View):
    template_name = 'registration/login.html'
    def get(self,request,*args,**kwargs):
        form = LoginForm()
        # form = AuthenticationForm() #django built in login form
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = LoginForm( data=request.POST)
        # form = AuthenticationForm(request, data=request.POST) #django built-in login form
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Login Successful for {user.username}')
                return redirect('profile-view')
        messages.error(request, 'Invalid Login Credentials')
        return render(request, self.template_name, {'form':form})
    
class SignUpView(View):
    template_name = 'registration/signup.html'
    def get(self,request,*args,**kwargs):
        # form = UserCreationForm() # get django built-in signup form
        form = SignupForm() 
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        # form = UserCreationForm(data=request.POST) #post from django built-in signup form
        form = SignupForm(data=request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('login')
        return render(request, self.template_name, {'form':form})

class ProfileTemplateView(LoginRequiredMixin,TemplateView,):
    template_name = 'registration/profile.html'
    login_url = 'login'

class RedirectUser(RedirectView):
    pattern_name = 'profile-view'
# class RedirectUser(RedirectView):
#     url = '/profile/'