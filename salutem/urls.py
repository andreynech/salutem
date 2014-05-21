from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'salutem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^publications/', include('publications.urls', namespace = 'publications')),
    url(r'^admin/', include(admin.site.urls)),
)
