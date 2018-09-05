from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


from . import models


class BlogListView(ListView):
    model = models.Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = models.Post
    template_name = 'blog_detail.html'


class BlogUpdateView(UpdateView):
    model = models.Post
    fields = ['title', 'body', 'picture']
    template_name = 'blog_edit.html'


class BlogDeleteView(DeleteView):
    model = models.Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')


class BlogCreateView(CreateView):
    model = models.Post
    template_name = 'article_new.html'
    fields = ['title', 'body', 'author', 'picture']
