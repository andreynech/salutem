from django.conf.urls import patterns, url
from publications import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
     # ex: /publications/articles/5/
    url(r'^articles/(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name='article'),

    url(r'^authors/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author'),
)
