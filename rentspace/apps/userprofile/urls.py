from django.conf.urls import url
from userprofile import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^register/$',views.create_user),
    url(r'^login/$',views.login_user),
    #url(r'^logout/$',views.logout_user),  # TODO not working
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^myaccount/$',TemplateView.as_view(template_name='myaccount.html')),

    url(r'^changepassword/$',TemplateView.as_view(template_name='changepassword.html')),
    url(r'^updatepassword/$',views.change_password),

    url(r'^editprofile/$',views.edit_profile),

    url(r'^resetpassword/$',views.reset_password),


    url(r'^test_task/$',views.test_task),
    url(r'^test_file_upload/$',views.test_file_upload),

    url(r'^register_success/$',views.register_success),


    # REST api
    url(r'^api/users/$', views.UserList.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/status/$', views.user_status),

    # TODO not implemented

    # url(r'^api/login/$',views.login_user),
    # url(r'^api/logout/$','django.contrib.auth.views.logout', {'next_page': '/'}),
   
]




urlpatterns = format_suffix_patterns(urlpatterns)

