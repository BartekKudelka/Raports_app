from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from . import views

from raports_generator import views as report_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^raports_generator/', include('raports_generator.urls')),
    url(r'^$', report_views.reports, name='home'),
    url(r'^sign_up/', views.sign_up, name="sign_up"),

    url(r'^login/$', LoginView, {'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', LogoutView, {'next_page': '/logged_out/'}, name="logout"),
    url(r'^logged_out/$', views.logged_out, name="logged_out"),
]
