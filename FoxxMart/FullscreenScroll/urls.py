from django.urls import path

from . import views

app_name = "FullscreenScroll"


urlpatterns = [
    #Leave as empty string for base url
	path('', views.store, name="store"),
]