from django.conf.urls import include, url
from django.contrib import admin
# from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^raports_generator/', include('raports_generator.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^sign_up/', views.sign_up, name="sign_up"),

    url(r'^login/$', login, {'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', logout, {'next_page': '/logged_out/'}, name="logout"),
    url(r'^logged_out/$', views.logged_out, name="logged_out"),

    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^profile/$', views.edit_profile, name='edit_profile'),
    ]


