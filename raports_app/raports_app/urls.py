"""raports_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^raports_generator/', include('raports_generator.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^sign_up/', views.sign_up, name="sign_up"),

    url(r'^login/$', LoginView, {'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', LogoutView, {'next_page': '/logged_out/'}, name="logout"),
    url(r'^logged_out/$', views.logged_out, name="logged_out"),
]
