from django.conf.urls import patterns, url, include

from webdjango import views
from webdjango import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api/recruitment$', views.recruitment, name='recruitment'),
    (r'^api/v2/', include('webdjango.api.urls')),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)