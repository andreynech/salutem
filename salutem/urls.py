from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
admin.autodiscover()

from salutem import views

urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'salutem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.HomeView.as_view(template_name='index.html'), name='home'),
    url(r'^publications/', include('publications.urls', namespace = 'publications')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
)
