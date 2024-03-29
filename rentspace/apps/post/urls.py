from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

urlpatterns = [
    
    url(r'^myposts$',views.myposts,name="myposts"),
    url(r'^addpost/?$',views.addpost,name="addpost"),
    url(r'^showpost/$',views.showpost,name="showpost"),
    url(r'^searchposts/$',views.searchposts,name="searchposts"),
    url(r'^updatepost/$',views.updatepost,name="updatepost"),
    
    url(r'^deletepost/$',views.deletepost,name="deletepost"),
    url(r'^activatepost/$',views.activatepost,name="activatepost"),

    url(r'^shortlistedposts/$',views.shortlistedposts,name="shortlistedposts"),

    url(r'^contactpostowner/$',views.contactpostowner,name="contactpostowner"),
    url(r'^shortlistpost/$',views.shortlistpost,name="shortlistpost"),
    url(r'^delistpost/$',views.delistpost,name="delistpost"),
    

    ### REST API ADMIN

    # url(r'^api/users/(?P<user_pk>[0-9]+)/posts/$', views.PostList.as_view()),
    # url(r'^api/users/(?P<user_pk>[0-9]+)/posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    # url(r'^api/users/(?P<user_pk>[0-9]+)/posts/(?P<pk>[0-9]+)/status/$', views.post_status),
    # url(r'^api/users/(?P<user_pk>[0-9]+)/posts/(?P<post_pk>[0-9]+)/attributes/$', views.PostAttributeList.as_view()),

    ## Rest api  (for mobile client)
    url('api/posts$',views.Posts.as_view()),  # Add post Get posts
    url('^api/posts/(?P<pk>[0-9]+)$', views.PostDetail.as_view()),  # Update post , Delete post
    url('^api/posts/(?P<pk>[0-9]+)/status$', views.post_status),    # Get status of post, Update status of posts
]


urlpatterns = format_suffix_patterns(urlpatterns)


