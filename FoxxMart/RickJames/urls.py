from django.urls import path
from . import views

app_name = "RickJames"

urlpatterns = [
    path('', views.store, name='store')
]
