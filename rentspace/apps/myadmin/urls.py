from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from myadmin import views
from django.views.generic import TemplateView

urlpatterns = [
    
    url(r'^admin/users$',views.getusers,name="admin_users"),
    url(r'^admin/posts$',views.getposts,name="admin_posts"),
    url(r'^admin$',TemplateView.as_view(template_name='admin_home.html'),name="admin_home"),
    
]


urlpatterns = format_suffix_patterns(urlpatterns)


