from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views
from django.views.generic import TemplateView
from django.conf.urls import *


urlpatterns = [
    #url(r'^$', views.index), 
    url(r'^$',TemplateView.as_view(template_name='index.html')),
    url(r'^about$',TemplateView.as_view(template_name='aboutus.html')),
    url(r'^contact$',TemplateView.as_view(template_name='contactus.html')),
    url(r'^support$',TemplateView.as_view(template_name='support.html')),
    url(r'^blog$',TemplateView.as_view(template_name='blog.html')),
    url(r'^careers$',TemplateView.as_view(template_name='careers.html')),
    url(r'^help$',TemplateView.as_view(template_name='help.html')),
    url(r'^faq$',TemplateView.as_view(template_name='faq.html')),
    url(r'^terms$',TemplateView.as_view(template_name='terms.html')),
    url(r'^reset$',TemplateView.as_view(template_name='reset_password.html')),
    url(r'^register$',TemplateView.as_view(template_name='register.html')),
    url(r'^login$',TemplateView.as_view(template_name='login.html')),

    url(r'^users/$', views.UserList.as_view()),



    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^users/(?P<pk>[0-9]+)/status/$', views.user_status),

    url(r'^users/(?P<user_pk>[0-9]+)/posts/$', views.PostList.as_view()),
    url(r'^users/(?P<user_pk>[0-9]+)/posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^users/(?P<user_pk>[0-9]+)/posts/(?P<pk>[0-9]+)/status/$', views.post_status),

    url(r'^users/(?P<user_pk>[0-9]+)/posts/(?P<post_pk>[0-9]+)/attributes/$', views.PostAttributeList.as_view()),


    url(r'^users/(?P<user_pk>[0-9]+)/posts/(?P<post_pk>[0-9]+)/images/$', views.ImageList.as_view()),
    url(r'^users/(?P<user_pk>[0-9]+)/posts/(?P<post_pk>[0-9]+)/images/(?P<pk>[0-9]+)/$', views.ImageDetail.as_view()),

    url(r'^images/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.ImageDownload.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


