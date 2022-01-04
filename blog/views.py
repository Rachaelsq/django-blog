from django.shortcuts import render
from django.urls.base import reverse
#CRUD imports
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

#redirect
from django.urls import reverse_lazy

#User auth imports
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Post
from django.views import generic
''' 
===================
blog 'POST' class
===================
'''

class BlogDetail(generic.DetailView):
    model = Post
    template_name = 'blog.html' 
    
''' class BlogDetail(DetailView):
    model = Post
    template_name = 'blog/blog.html' '''