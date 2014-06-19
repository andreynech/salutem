from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

from publications.models import Article, Author


class IndexView(generic.ListView):
    model = Article
    paginate_by = 20

    def get_queryset(self):
                 
        if 'search' in self.request.GET:
            objects = self.model.objects.filter(
                headline__icontains = self.request.GET['search']
                # | Q(....)
                )
        else:
            objects = self.model.objects.all()
         
        return objects

#    def get_queryset(self):
#        """Return the last five published articles."""
#        return Article.objects.order_by('-submit_date')[:5]

class AuthorList(generic.ListView):
    model = Author
    paginate_by = 20

    def get_queryset(self):
                 
        if 'search' in self.request.GET:
            objects = self.model.objects.filter(
                Q(first_name__icontains = self.request.GET['search'])
                | Q(last_name__icontains = self.request.GET['search'])
                | Q(organization__icontains = self.request.GET['search'])
                )
        else:
            objects = self.model.objects.all()
         
        return objects


class ArticleDetailView(generic.DetailView):
    model = Article


class AuthorDetailView(generic.DetailView):
    model = Author

###########################################

class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'title', 'email', 'organization']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthorCreate, self).dispatch(*args, **kwargs)


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'title', 'email', 'organization']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthorUpdate, self).dispatch(*args, **kwargs)


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('publications:authorindex')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthorDelete, self).dispatch(*args, **kwargs)

###########################################

class ArticleCreate(CreateView):
    model = Article
    fields = ['headline', 'authors', 'abstract', 'abstract_en', 'article_url']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArticleCreate, self).dispatch(*args, **kwargs)

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['headline', 'authors', 'abstract', 'abstract_en']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArticleUpdate, self).dispatch(*args, **kwargs)


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('publications:articleindex')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArticleDelete, self).dispatch(*args, **kwargs)
