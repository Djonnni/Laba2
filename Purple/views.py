# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView, View
from django.shortcuts import redirect
from models import Trip, Plane, Passport_data, Tickets
#from django.contrib import admin


class Passport_dataView(View):
      template_name = "index.html"

      def post(self, *args, **kwargs):
        surname_value = self.request.POST['surname']
        name_value = self.request.POST['name']
        pytronymic_value = self.request.POST['pytronymic']
        Passport_data.objects.create(surname=surname_value, name=name_value, pytronymic=pytronymic_value)
        return  redirect('/')


class DeletePassport_data(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        fio_delete = self.request.POST['delete_fio']
        Passport_data.objects.filter(id=int(fio_delete)).delete()
        return redirect('/')


class PlanesView(View):
    template_name = "index.html"

    def post(self, *args,**kwargs):
        airline_value = self.request.POST['airline']
        privileges_value = self.request.POST['privileges']
        type_of_plane_value = self.request.POST['type_of_plane']
        place_count_value = self.request.POST['place_count']
        Plane.objects.create(
            airline=airline_value,
            privileges=privileges_value,
            type_of_plane=type_of_plane_value,
            place_count=place_count_value
        )
        return redirect('/')


class DeletePlane(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        plane_delete = self.request.POST['delete_plane']
        Plane.objects.filter(id=int(plane_delete)).delete()
        return redirect('/')


class TripsView(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        point_of_departure_value = self.request.POST['point_of_departure']
        point_of_destination_value = self.request.POST['point_of_destination']
        data_of_departure_value = self.request.POST['data_of_departure']
        time_of_departure_value = self.request.POST['time_of_departure']
        data_of_destination_value = self.request.POST['data_of_destination']
        time_of_destination_value = self.request.POST['time_of_destination']
        plane_number_value = self.request.POST['plane_number']
        cost_value = self.request.POST['cost']
        Trip.objects.create(
            point_of_departure=point_of_departure_value,
            point_of_destination=point_of_destination_value,
            data_of_departure=data_of_departure_value,
            time_of_departure=time_of_departure_value,
            data_of_destination=data_of_destination_value,
            time_of_destination=time_of_destination_value,
            plane_number=Plane.objects.filter(id=int(plane_number_value))[0],
            cost=cost_value
        )
        return redirect('/')


class DeleteTrip(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        trip_delete = self.request.POST['delete_trip']
        Trip.objects.filter(id=int(trip_delete)).delete()
        return redirect('/')


class TicketsView(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        trip_number_value = self.request.POST['trip_number']
        passenger_id_value = self.request.POST['passenger_id']
        ticket_id_value = self.request.POST['ticket_id']
        purchase_data_value = self.request.POST['purchase_data']
        purchase_time_value = self.request.POST['purchase_time']
        purchase_cost_value = self.request.POST['purchase_cost']
        Tickets.objects.create(
            trip_number=Trip.objects.filter(id=int(trip_number_value))[0],
            passenger_id=Passport_data.objects.filter(id=int(passenger_id_value))[0],
            ticket_id=ticket_id_value,
            purchase_data=purchase_data_value,
            purchase_time=purchase_time_value,
            purchase_cost=purchase_cost_value
        )
        return redirect('/')


class DeleteTicket(View):
    template_name = "index.html"

    def post(self, *args,  **kwargs):
        ticket_delete = self.request.POST['delete_ticket']
        Tickets.objects.filter(id=int(ticket_delete)).delete()
        return redirect('/')


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        passport_data_list = Passport_data.objects.all()
        trip_list = Trip.objects.all()
        plane_list = Plane.objects.all()
        tickets_list = Tickets.objects.all()
        context.update(
            {
                'passport_data_list': passport_data_list,
                'trip_list': trip_list,
                'plane_list': plane_list,
                'tickets_list': tickets_list,
            }
        )
        return context