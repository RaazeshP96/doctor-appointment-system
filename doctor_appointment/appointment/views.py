from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Doctor


class DoctorList(ListView):
    model = Doctor


class DoctorDetail(DetailView):
    model = Doctor
    queryset = Doctor.objects.all()


