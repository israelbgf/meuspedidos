from django.conf.urls import patterns, url

from webdjango import views
from webdjango import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api/recruitment$', views.recruitment, name='recruitment'),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)