from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('', views.index,name='home'),
    path("about-us/", views.aboutUs, name="about-us"),
    path("contact-us/", views.contactUs, name="contact-us"),
    path("projects/", views.projects, name="projects"),
    path("shop/", views.shop, name="shop"),
    path("solutions/", views.solutions, name="solutions"),
    # path('', include("django.contrib.auth.urls")),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)