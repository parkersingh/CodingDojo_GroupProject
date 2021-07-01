from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('game', views.game),
    path('create', views.create),
    path('hit', views.hit),
    path('tutorial', views.tutorial),
]