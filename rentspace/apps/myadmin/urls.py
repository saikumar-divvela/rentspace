from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from myadmin import views
from django.views.generic import TemplateView

urlpatterns = [

	# urls for user management
	url(r'^admin$',TemplateView.as_view(template_name='admin_home.html'),name="admin_home"),
    url(r'^admin/users/all$',views.all_users,name="all_users"),
	url(r'^admin/users/inactive$',views.inactive_users,name="inactive_users"),

    url(r'^verifyidcard$',views.verifyidcard,name="verifyidcard"),
    url(r'^verifyphone$',views.verifyphone,name="verifyphone"),


    url(r'^admin/posts/all$',views.all_posts,name="all_posts"),
	url(r'^admin/posts/unverified$',views.unverified_posts,name="unverified_posts"),
	url(r'^admin/posts/inactive$',views.inactive_posts,name="inactive_posts"),
	url(r'^admin/posts/images$',views.post_images,name="post_images"),



    url(r'^admin/posts/verifypost$',views.verifypost,name="verifypost"),
]


urlpatterns = format_suffix_patterns(urlpatterns)


