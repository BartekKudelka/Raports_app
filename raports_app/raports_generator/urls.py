from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^reports/', views.reports, name="reports"),
    url(r'^create_report/', views.create_report, name="create_report"),
    url(r'^show_visual_report/(?P<id>\d+)/$', views.show_visual_report, name='show_visual_report'),
    url(r'^show_text_report/(?P<id>\d+)/$', views.show_text_report, name='show_text_report'),

    url(r'^edit_report/(?P<id>\d+)/$', views.edit_report, name='edit_report'),

    url(r'^delete_report/(?P<id>\d+)/$', views.delete_report, name='delete_report'),
]
