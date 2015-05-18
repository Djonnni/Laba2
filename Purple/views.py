# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from models import Trip, Plane, Passport_data, Tickets
from django.contrib import admin

passport_data_list = Passport_data.objects.all()
trip_list = Trip.objects.all()
plane_list = Plane.objects.all()
tickets_list = Tickets.objects.all()


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'passport_data_list': passport_data_list,
                'trip_list': trip_list,
                'plane_list': plane_list,
                'tickets_list': tickets_list,
            }
        )
        return context