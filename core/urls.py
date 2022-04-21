from django.urls import path

from .views import IndexView, TwCompView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projetos/twcomp/', TwCompView.as_view(), name='twcomp')
]