from django.urls import path

from . import views

app_name = 'looker_upper'

urlpatterns = [
    path('', views.index, name='index'),
    path('find/', views.find, name='find'),
]