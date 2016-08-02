from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    #url(r'^$', views.index), 
    url(r'^$',TemplateView.as_view(template_name='index.html')),
    url(r'^home$',TemplateView.as_view(template_name='index.html'),name="home"),
    url(r'^index.html/$',TemplateView.as_view(template_name='index.html'),name="home"),

    url(r'^signin/?$',TemplateView.as_view(template_name='signin.html'),name="signin"),
    url(r'^signup/?$',TemplateView.as_view(template_name='signup.html'),name="signup"),

    url(r'^about$',TemplateView.as_view(template_name='aboutus.html'),name="aboutus"),
    url(r'^contact$',TemplateView.as_view(template_name='contactus.html'),name="contact"),
    url(r'^support$',TemplateView.as_view(template_name='support.html'),name="support"),
    url(r'^blog$',TemplateView.as_view(template_name='blog.html'),name="blog"),
    url(r'^careers$',TemplateView.as_view(template_name='careers.html'),name="careers"),

    url(r'^help$',TemplateView.as_view(template_name='help.html'),name="help"),
    url(r'^faq$',TemplateView.as_view(template_name='faq.html'),name="faq"),
    url(r'^terms$',TemplateView.as_view(template_name='terms.html'),name="terms"),


    
]




