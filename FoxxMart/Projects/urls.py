from django.urls import path

from . import views

app_name = "Projects"


urlpatterns = [
    #Leave as empty string for base url
	path('IDACA/', views.IDACA, name="IDACA"),
	path('IDACA/Gallery', views.gallery, name="gallery"),
	path('BrandCentral/', views.bc, name="bc"),
	path('AfricanUs/', views.africanus, name="africanus"),
	path('AfricanUs/About', views.about, name="about"),
	path('AfricanUs/Services', views.services, name="services"),
	path('AfricanUs/Contact', views.contact, name="contact"),


]
