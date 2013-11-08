from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import *
urlpatterns = patterns("",
	url(r"get/", get_status, name="get_netstatus"),
    url(r"^$", TemplateView.as_view(template_name="netstatus.html"), name="netstatus"),
    )
