from django.urls import path
from . import views

app_name = 'sequence'

urlpatterns = [
    path('/elem/<int:pk>',
         views.generate_following_sequence, name='generate_following_sequence'),
    path('/longest/<int:pk>',
         views.returns_the_value_smaller_than_n, name='generate_following_sequence'),
]