from django.conf.urls import patterns, url
from publications import views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^articles/$', views.IndexView.as_view(), name='articleindex'),
     # ex: /publications/articles/5/
    url(r'^articles/(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name='article_detail'),

    #url(r'^articles/add/$', views.ArticleCreate.as_view(), name='article_add'),
    url(r'^articles/add/$', login_required(views.ArticleWizard.as_view(views.FORMS)), name='article_add'),


    url(r'^articles/(?P<pk>\d+)/update/$', views.ArticleUpdate.as_view(), name='article_update'),
    url(r'^articles/(?P<pk>\d+)/delete/$', views.ArticleDelete.as_view(), name='article_delete'),

    url(r'^authors/$', views.AuthorList.as_view(), name='authorindex'),
    url(r'^authors/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author_detail'),

    #url(r'^authors/add/$', views.AuthorCreate.as_view(), name='author_add'),
    url(r'^authors/add/$', views.AuthorCreate, name='author_add'),

    url(r'^authors/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^authors/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
)
