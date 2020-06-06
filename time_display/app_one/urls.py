from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    # path('',view.displaytime),
    path('time_display',views.displaytime),
]