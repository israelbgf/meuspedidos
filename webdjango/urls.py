from django.conf.urls import patterns, url

from webdjango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api/recruitment$', views.recruitment, name='recruitment'),
)