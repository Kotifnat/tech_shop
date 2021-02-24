from django.shortcuts import render
from django.views.generic import DetailView
from .models import CustomUser
# Create your views here.


class UserProfile(DetailView):
    model = CustomUser
    template_name = 'users/user_detail.html'
