from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from app.models import *
# Create your views here.


class Home(TemplateView):
    template_name='app/home.html'



class SchoolList(ListView):
    model=School
    template_name='school_list.html'
    context_object_name='schools'