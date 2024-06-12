from django.urls import path
from .views import *
urlpatterns = [
    path(f'results/' , resultView.as_view() , name="add")
]