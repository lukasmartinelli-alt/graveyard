from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login
from front import views
from registration.views import register_domain

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mailgenic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.Home.as_view(), name="home"),
    url(r'^registration/domain/$', register_domain, name="register"),
    url(r'^admin/', include(admin.site.urls)),
)
