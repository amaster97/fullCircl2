"""fullcircle URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from fullcircle.views import home, signup, login_views, logout_views, method, signupSeeker, signupRecruiter, matches, pending, update_profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^signup/seeker$', signupSeeker, name='signupSeeker'),
    url(r'^signup/recruiter$', signupRecruiter, name='signupRecruiter'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', logout_views, name='logout'),
    url(r'^accounts/profile/$', home, name='dashboard'),
    url(r'^dashboard/$', home, name='dashboard'),
    url(r'^matches/$', matches, name='matches'),
    url(r'^pending/$', pending, name='pending'),
    url(r'^profile/$', update_profile, name='update_profile'),
    url(r'^method/$', method, name='method'),
]
