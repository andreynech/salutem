from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

from salutem import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'salutem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.HomeView.as_view(template_name='index.html'), name='home'),
    url(r'^publications/', include('publications.urls', namespace = 'publications')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
)
