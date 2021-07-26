from django.shortcuts import redirect
from django.views.generic import TemplateView

class HomePageViews(TemplateView):
    template_name = 'home.html'


class AboutPageViews(TemplateView):
    template_name = 'about.html'



class BaseVieews(TemplateView):
    template_name = 'base.html'

class AsdViews(TemplateView):
    template_name = 'asd.html'