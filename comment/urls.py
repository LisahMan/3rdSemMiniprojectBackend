from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$',views.CommentCreate.as_view()),
    url(r'^delete/(?P<pk>[0-9]+)/$',views.CommentDelete.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$',views.CommentOfPost.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)