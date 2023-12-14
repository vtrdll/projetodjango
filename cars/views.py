from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelform
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 
# Create your views here.


class CarsView(View):
    def get(self, request):
        search = request.GET.get('search')
        cars =  Car.objects.all().order_by('model')

        if search:
            cars = Car.objects.filter(model__icontains=search)

        return render(request,'cars.html', {'cars': cars })

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = Car.objects.filter(model__icontains=search)
        return cars

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class= CarModelform
    template_name = 'new_car.html'
    success_url = '/cars_list/'

class CarDetailView(DetailView):
    model = Car 
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class= CarModelform
    template_name= 'car_update.html'
    

    def get_success_url(self) :
        return  reverse_lazy('car_detail', kwargs = {'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'