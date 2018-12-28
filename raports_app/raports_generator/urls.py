from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^reports/', views.reports, name="reports"),
    url(r'^create_report/', views.create_report, name="create_report"),
]