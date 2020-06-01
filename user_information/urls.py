from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$',views.UserCollection.as_view()),
    url(r'^(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
    url(r'^login/$',views.CheckUserDetail.as_view()),
    url(r'^search/(?P<pk>[0-9]+)/$',views.SearchUser.as_view()),
    url(r'^following/(?P<pk>[0-9]+)/$',views.FollowerOfUser.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)