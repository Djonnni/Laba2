from django.conf.urls import patterns, url

from django.contrib import admin

from views import IndexView, Passport_dataView, DeletePassport_data, PlanesView, DeletePlane, TripsView, DeleteTrip, TicketsView, DeleteTicket


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^Passport_data', Passport_dataView.as_view()),
    url(r'^delete_fio', DeletePassport_data.as_view()),
    url(r'^Plain', PlanesView.as_view()),
    url(r'^delete_plane', DeletePlane.as_view()),
    url(r'^Trip', TripsView.as_view()),
    url(r'^delete_trip', DeleteTrip.as_view()),
    url(r'^Ticket', TicketsView.as_view()),
    url(r'^delete_ticket', DeleteTicket.as_view()),
    url(r'^$', IndexView.as_view()),
)