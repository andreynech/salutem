from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from publications.models import Article, Author


class IndexView(generic.ListView):
    model = Article

#    def get_queryset(self):
#        """Return the last five published articles."""
#        return Article.objects.order_by('-submit_date')[:5]


class ArticleDetailView(generic.DetailView):
    model = Article


class AuthorDetailView(generic.DetailView):
    model = Author


#def index(request):
#    latest_article_list = Article.objects.order_by('-submit_date')[:5]
#    context = {'latest_article_list': latest_article_list}
#    return render(request, 'publications/index.html', context)
#
#
#def article(request, article_id):
#    art = get_object_or_404(Article, pk=article_id)
#    return render(request, 'publications/article.html', {'article': art})
#
#
#def author(request, author_id):
#    aut = get_object_or_404(Author, pk=author_id)
#    return render(request, 'publications/author.html', {'author': aut})
