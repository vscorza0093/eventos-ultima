from django.contrib import admin
from django.urls import path
from eventos.views import inicio

urlpatterns = [
    path('', inicio),
    path("admin/", admin.site.urls),
]
