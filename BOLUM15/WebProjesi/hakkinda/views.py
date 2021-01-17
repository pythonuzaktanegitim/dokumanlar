from django.shortcuts import render
from django.views.generic import TemplateView

class Hakkinda(TemplateView):
    template_name = "hakkinda.html"