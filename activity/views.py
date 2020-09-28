from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Posts
from .forms import PostCreateForm
# Create your views here.


#@login_required
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['description', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostListView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'activity/timeline.html'
    context_object_name = 'posts'
    ordering = ['-created']


class PostDetailView(DetailView):
    model = Posts


