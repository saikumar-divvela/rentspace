from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    #url(r'^$', views.index), 
    url(r'^$',TemplateView.as_view(template_name='index.html')),
    url(r'^home/$',TemplateView.as_view(template_name='index.html')),
    url(r'^index.html/$',TemplateView.as_view(template_name='index.html')),

    url(r'^signin/$',TemplateView.as_view(template_name='signin.html')),
    url(r'^signup/$',TemplateView.as_view(template_name='signup.html')),

    url(r'^about$',TemplateView.as_view(template_name='aboutus.html')),
    url(r'^contact$',TemplateView.as_view(template_name='contactus.html')),
    url(r'^support$',TemplateView.as_view(template_name='support.html')),
    url(r'^blog$',TemplateView.as_view(template_name='blog.html')),
    url(r'^careers$',TemplateView.as_view(template_name='careers.html')),

    url(r'^help$',TemplateView.as_view(template_name='help.html')),
    url(r'^faq$',TemplateView.as_view(template_name='faq.html')),
    url(r'^terms$',TemplateView.as_view(template_name='terms.html')),
]




