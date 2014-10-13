from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login
from front import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mailgenic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.Home.as_view(), name="home"),
    url(r'^register/$', views.Register.as_view(), name="register"),
    url(r'^admin/', include(admin.site.urls)),
)
