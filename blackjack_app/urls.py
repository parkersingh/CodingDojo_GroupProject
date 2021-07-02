from django.urls import path
from . import views

urlpatterns = [
    path('', views.age_check),
    path('validate_age', views.validate_age),
    path('index', views.index),
    path('game', views.game),
    path('create', views.create),
    path('hit', views.hit),
    path('tutorial', views.tutorial),
    path('age_check', views.age_check),
    path('validate_age', views.validate_age),
    path('hit',views.hit),
    path('stand', views.stand)
]