# Django 
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

# Models 
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

# Forms 
from users.forms import SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    queryset = User.objects.all()

    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["posts"] = Post.objects.filter(user=user).order_by('-created')
        return context
    

class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['profile_picture', 'website', 'bio', 'phone_number']
    success_url = reverse_lazy('posts:feed')

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username' : username})


class LoginView(auth_views.LoginView):
    
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):

    template_name = 'logged_out.html'
