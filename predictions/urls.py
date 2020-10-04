from django.urls import path
from . import views

urlpatterns = [
    path('past_data', views.past_data, name='past_data'),
    path('input_data', views.input_data, name='input_data'),
    path('test_patient', views.test_patient, name='test_patient'),
]