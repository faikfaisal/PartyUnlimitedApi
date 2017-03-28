from django.conf.urls import url

from guestlist import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^venues/$', views.VenueList.as_view(), name='venue-list'),
    url(r'^venues/(?P<pk>[0-9]+)/$', views.VenueDetail.as_view(), name='venue-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^parties/$', views.PartyList.as_view(), name='party-list'),
    url(r'^parties/(?P<pk>[0-9]+)/$', views.PartyDetails.as_view(), name='party-detail'),
    url(r'^guestlist/$', views.GuestListList.as_view(), name='guestlist-list'),
    url(r'^guestlist/(?P<pk>[0-9]+)/$', views.GuestListDetail.as_view(), name='guestlist-detail'),
]
