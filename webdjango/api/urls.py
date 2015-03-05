from django.conf.urls import patterns, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from webdjango.api.handlers import EvaluationFormHandler


auth = HttpBasicAuthentication(realm="My Realm")
ad = {'authentication': auth}

evaluation_form_resource = Resource(handler=EvaluationFormHandler)

urlpatterns = patterns('',
                       url(r'^recruitment/', evaluation_form_resource),
)