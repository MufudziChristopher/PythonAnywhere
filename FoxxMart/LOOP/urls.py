from django.urls import path

from . import views

app_name = "Loop"


urlpatterns = [
    #Leave as empty string for base url
	path('', views.store, name="store"),
]