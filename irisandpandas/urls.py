from django.urls import path
from . import views

app_name = 'iris'

urlpatterns = [
    path('/group/sepal_length/max', views.sepal_length_max, name='sepal_length_max'),
    path('/describe',
         views.describe, name='describe'),
]