from django.urls import path 

from . import views

app_name = "COURT"

urlpatterns = [
	path('', views.store, name="store"),
]
