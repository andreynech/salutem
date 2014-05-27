from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms

from publications.models import Article, Author


class IndexView(generic.ListView):
    model = Article

#    def get_queryset(self):
#        """Return the last five published articles."""
#        return Article.objects.order_by('-submit_date')[:5]

class AuthorList(generic.ListView):
    model = Author


class ArticleDetailView(generic.DetailView):
    model = Article


class AuthorDetailView(generic.DetailView):
    model = Author

###########################################

class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'title', 'email', 'organization']

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'title', 'email', 'organization']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('publications:authorindex')

###########################################

class ArticleCreate(CreateView):
    model = Article
    fields = ['headline', 'authors', 'submit_date', 'abstract', 'abstract_en']

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['headline', 'authors', 'submit_date', 'abstract', 'abstract_en']


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('publications:articleindex')
