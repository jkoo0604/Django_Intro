from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reset', views.reset_score),
    path('target', views.set_target),
    path('<str:location>', views.process_money)

]