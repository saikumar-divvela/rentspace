from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
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
