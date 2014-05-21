from django.shortcuts import render, get_object_or_404

from publications.models import Article, Author


def index(request):
    latest_article_list = Article.objects.order_by('-submit_date')[:5]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'publications/index.html', context)


def article(request, article_id):
    art = get_object_or_404(Article, pk=article_id)
    return render(request, 'publications/article.html', {'article': art})


def author(request, author_id):
    aut = get_object_or_404(Author, pk=author_id)
    return render(request, 'publications/author.html', {'author': aut})
