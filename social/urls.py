from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^create/$',views.SocialCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/following/$',views.SocialFollowingGet.as_view()),
    url(r'^(?P<pk>[0-9]+)/followers/$',views.SocialFollowerGet.as_view()),
    url(r'^delete/(?P<fk>[0-9]+)/(?P<pk>[0-9]+)/$',views.SocialDelete.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)