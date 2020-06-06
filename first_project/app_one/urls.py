from django.urls import path

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('new', views.new),
    path('create',views.create),
    path('<int:my_int>',views.show),
    path('<int:my_int>/edit',views.edit),
    path('<int:my_int>/delete',views.destroy),
    path('<str:name>', views.hello_name),
]