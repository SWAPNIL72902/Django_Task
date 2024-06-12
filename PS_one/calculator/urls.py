from django.urls import path
from .views import *
urlpatterns = [
    path(f'add/' , addView.as_view() , name="add"),
    path(f'subtract/' , subView.as_view() , name="subtract"),
    path(f'multiply/' , multiplyView.as_view() , name="multiply"),
    path(f'divide/' , divideView.as_view() , name="divide"),
]
