from django.urls import path
from . import views

app_name='sample'

urlpatterns = [
    path('', views.sample_choice_view, name='sample_choice'),
]
