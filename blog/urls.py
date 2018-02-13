from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^cate/(?P<pk>[0-9]+)/$', views.memory, name='memory'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.cate_list, name='cate_list')
]
