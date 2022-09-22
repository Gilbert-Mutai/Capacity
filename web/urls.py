from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('', views.index,name='home'),
    # path('', include("django.contrib.auth.urls")),
    # path("register/", views.register, name="register"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)