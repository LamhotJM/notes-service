from django.conf.urls import patterns, url
from commentengine import views

urlpatterns = patterns('',
                       url(r'comments/$', views.MasterCommentList.as_view()),
                       url(r'^comments/(?P<pk>[0-9]+)/$', views.MasterCommentDetail.as_view()),
                       )
