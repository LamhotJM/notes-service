from django.conf.urls import patterns, url
from commentengine import apiviews

urlpatterns = patterns('',
                       url(r'comments/$', apiviews.MasterCommentList.as_view()),
                       url(r'^comments/(?P<pk>[0-9]+)/$', apiviews.MasterCommentDetail.as_view()),
                       )
