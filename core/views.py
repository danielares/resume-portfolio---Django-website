from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    
class TwCompView(TemplateView):
    template_name = 'twcomp.html'
    
class TodoWickView(TemplateView):
    template_name = 'todo-wick.html'