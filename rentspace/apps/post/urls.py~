from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

urlpatterns = [
    
    url(r'^posts/$',views.showallpost),
    url(r'^addpost/$',views.addpost),
    url(r'^showpost/$',views.showpost),
    url(r'^updatepost/$',views.updatepost),
    url(r'^deletepost/$',views.deletepost),

    ### REST API
    url(r'^api/users/(?P<user_pk>[0-9]+)/posts/$', views.PostList.as_view()),
    url(r'^api/users/(?P<user_pk>[0-9]+)/posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^api/users/(?P<user_pk>[0-9]+)/posts/(?P<pk>[0-9]+)/status/$', views.post_status),
    url(r'^api/users/(?P<user_pk>[0-9]+)/posts/(?P<post_pk>[0-9]+)/attributes/$', views.PostAttributeList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


