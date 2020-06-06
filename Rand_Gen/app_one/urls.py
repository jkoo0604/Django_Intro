from django.urls import path
from . import views

urlpatterns = [
    path('',views.generateword),
    path('random_word',views.generateword),
    path('reset',views.resetcounter)
]