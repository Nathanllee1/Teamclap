from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body', 'picture']
    template_name = 'blog_edit.html'
    success_url = reverse_lazy('home')
    login_url = 'login'


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'article_new.html'
    fields = ['title', 'body', 'picture']
    success_url = reverse_lazy('home')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        #return super().form_valid(form)

