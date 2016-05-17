from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^users/(?P<pk>[0-9]+)/status/$', views.user_status),

    url(r'^users/(?P<user_pk>[0-9]+)/posts/$', views.PostList.as_view()),
    url(r'^users/(?P<user_pk>[0-9]+)/posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
