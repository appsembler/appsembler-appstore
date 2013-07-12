from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import AppCategoryDetailView, ApplicationDetailView

urlpatterns = patterns('',
    url(r'^application/(?P<pk>\d+)/$', ApplicationDetailView.as_view(), name='appstore_application_detail'),
    url(r'^category/(?P<slug>\w+)/$', AppCategoryDetailView.as_view(), name='appstore_appcategory_detail'),
    url(r'^$', TemplateView.as_view(template_name='appstore/index.html'), name='appstore_index'),
)
