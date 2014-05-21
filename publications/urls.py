from django.conf.urls import patterns, url
from publications import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
     # ex: /publications/articles/5/
    url(r'^articles/(?P<article_id>\d+)/$', views.article, name='article'),

    url(r'^authors/(?P<author_id>\d+)/$', views.author, name='author'),
)
