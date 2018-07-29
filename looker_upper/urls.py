from django.urls import path

from . import views

app_name = 'looker_upper'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('find/', views.FindView.as_view(), name='find'),
]
