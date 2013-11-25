from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import *
urlpatterns = patterns("",
	url(r"get/", get_status, name="get_netstatus"),
	url(r"connect/(?P<ibsartu_id>\d+)/",send_ibsartu_file,name="ibsartu_file"),
	url(r"reset/(?P<ibsartu_id>\d+)/",reset_ibsartu_file,name="ibsartu_reset"),
    url(r"^$", TemplateView.as_view(template_name="netstatus.html"), name="netstatus"),
    )
