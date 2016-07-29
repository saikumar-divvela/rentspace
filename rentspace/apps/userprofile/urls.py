from django.conf.urls import url
from userprofile import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from rest_framework.authtoken import views as views1

urlpatterns = [
    
    url(r'^register$',views.create_user,name="register"),
    url(r'^login/?$',views.login_user,name="login"),
    #url(r'^logout/$',views.logout_user),  # TODO not working
    url(r'^logout/?$', 'django.contrib.auth.views.logout', {'next_page': '/'},name="logout"),
    url(r'^myaccount$',TemplateView.as_view(template_name='myaccount.html'),name="myaccount"),
    url(r'^changepassword$',TemplateView.as_view(template_name='changepassword.html'),name="change_password"),
    url(r'^updatepassword$',views.change_password,name="update_password"),
    url(r'^resetpassword$',views.reset_password,name="reset_password"),

    url(r'^editprofile$',views.edit_profile,name="edit_profile"),
    url(r'^register_success$',views.register_success,name="register_success"),
    url(r'^test_login$',views.test_login,name="test_login"),
    url(r'^test_file_upload$',views.test_file_upload,name="test_file_upload"),
   


    # REST api  (ADMIN)
    
    # url(r'^api/users$', views.UserList.as_view()),
    # url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    # url(r'^api/users/(?P<pk>[0-9]+)/status$', views.user_status),
    
    
    # REST api for mobile client / logged in user
    url(r'^api/register$', views.registeruser),  #POST
    url(r'^api/login$', views.userlogin),   #POST
    url(r'^api/logout$', views.userlogout),   # GET
    url(r'^api/testlogin$', views.testlogin),    # GET
    url(r'^api/userstatus$', views.user_status),  # GET PUT
    url(r'^api/profile$', views.user_profile,name="edit_profile1"),    # PUT
    url(r'^api-token-auth$', views1.obtain_auth_token),

    # REST api for testing
    url(r'^api/photoid$', views.photoid),  #POST
    
]




urlpatterns = format_suffix_patterns(urlpatterns)

