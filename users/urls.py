from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('past_data', views.past_data, name='past_data'),
    path('input_data', views.input_data, name='input_data'),
]