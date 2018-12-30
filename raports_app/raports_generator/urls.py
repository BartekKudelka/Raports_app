from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^reports/', views.reports, name="reports"),
    url(r'^create_report/', views.create_report, name="create_report"),
    url(r'^show_visual_report/(?P<id>\d+)/$', views.show_visual_report, name='show_visual_report')
]
