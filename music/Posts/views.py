from django.shortcuts import render
from django.views import generic
from Database import models as md

from django.views.generic import DetailView

from braces.views import SelectRelatedMixin



class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = md.Post





# Create your views here.
