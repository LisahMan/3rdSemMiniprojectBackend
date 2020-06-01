from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$',views.PostCollection.as_view()),
    url(r'^(?P<pk>[0-9]+)/$',views.PostDetail.as_view()),
    url(r'user/(?P<pk>[0-9]+)/$',views.PostOfUser.as_view()),
    url(r'userfeed/(?P<pk>[0-9]+)/$',views.PostOfFollowing.as_view()),
    url(r'save/$',views.PostSave.as_view()),
    url(r'unsave/(?P<fk>[0-9]+)/(?P<pk>[0-p]+)/$',views.PostUnsave.as_view()),
    url(r'savedpost/(?P<pk>[0-9]+)/',views.SavedPostOfUser.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)