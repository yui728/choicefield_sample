from django.urls import path
from . import views

app_name='sample'

urlpatterns = [
    path('sample1/', views.sample_choice_view, name='sample_choice'),
    path('sample2/', views.sample_choice_add_view, name='sample_choice_add'),
]
