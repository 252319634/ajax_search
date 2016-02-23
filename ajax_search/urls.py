from django.conf.urls import patterns, include, url
# from django.contrib import admin
from search import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ajax_search.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^search/$', views.search),
    url(r'^match/$', views.match),

)
