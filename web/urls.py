from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('', views.index,name='home'),
    path("about-us/", views.aboutUs, name="about-us"),
    path("contact-us/", views.contactUs, name="contact-us"),
    path("programmes/", views.programmes, name="programmes"),

    path("programme/agritech", views.agritech, name="agritech"),
    path("programme/employment", views.employment, name="employment"),
    path("programme/energy", views.energy, name="energy"),

    path("programme/construction", views.construction, name="construction"),
    path("programme/fintech", views.fintech, name="fintech"),
    path("programme/education", views.education, name="education"),

    path("programme/mobility", views.mobility, name="mobility"),
    path("programme/health", views.health, name="health"),
    path("programme/environment", views.environment, name="environment"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)