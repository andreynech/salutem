from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.contrib.formtools.wizard.views import SessionWizardView


from publications.models import Article, Author, ArticleAuthors


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

class AuthorCreate(ModelForm):

    class Meta:
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

class ArticleCreate(ModelForm):

    class Meta:
        model = Article
        #fields = ['headline', 'authors', 'abstract', 'abstract_en', 'article_url']
        fields = ['headline', 'abstract', 'abstract_en', 'article_url']

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



ARTICLE_WIZARD_FORMS = [("authors", formset_factory(AuthorCreate, max_num=5, can_delete=False)),
                        ("article", ArticleCreate),
                        ]


class ArticleWizard(SessionWizardView):

    TEMPLATES = {"authors": "publications/author_formset_form.html",
                 "article": "publications/article_form.html",
                 }

    def get_template_names(self):
        return [self.TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        #do_something_with_the_form_data(form_list)
        print([form.cleaned_data for form in form_list])

        articledata = self.get_cleaned_data_for_step('article')
        print("Article:")
        print(articledata)
        art = Article(**articledata)
        art.save()

        authordata = self.get_cleaned_data_for_step('authors')
        print("Authors:")
        print(authordata)
        pos = 0
        for aut_data in authordata:
            aut = Author(**aut_data)
            aut.save()
            aa = ArticleAuthors(article = art, author = aut, position = pos)
            aa.save()
            pos += 1

        return HttpResponseRedirect(reverse('publications:articleindex'))
