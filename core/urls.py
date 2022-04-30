from django.urls import path

from .views import IndexView, TwCompView, TodoWickView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projetos/twcomp/', TwCompView.as_view(), name='twcomp'),
    path('projetos/todo-wick/', TodoWickView.as_view(), name='todo-wick'),
]