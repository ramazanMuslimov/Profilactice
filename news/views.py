from datetime import datetime
from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )

from .models import Post
from .forms import ArticleForm, PostForm
from .filters import PostFilter



class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news/posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = PostFilter(self.request.GET, queryset)
       return self.filterset.qs
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context


# Поиск новостей через отдельную страницу 'search'
class PostSearch(ListView):
    model = Post
    template_name = 'news/post_search.html'
    context_object_name = 'post_search'

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = PostFilter(self.request.GET, queryset)
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context



class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_update.html'



class PostDelete(DeleteView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy('post_list')



# Артиклы
class ArticleList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news/article.html'
    context_object_name = 'posts'
    paginate_by = 10


class ArticleDetail(ListView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'


class ArticleCreate(CreateView):
    form_class = ArticleForm
    model = Post
    template_name = 'news/article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)


class ArticleDelete(DeleteView):
    form_class = ArticleForm
    model = Post
    template_name = 'news/article_delete.html'
    success_url = ('post_list')


class ArticleUpdate(UpdateView):
    form_class = ArticleForm
    model = Post
    template_name = 'news/article_edit.html'

