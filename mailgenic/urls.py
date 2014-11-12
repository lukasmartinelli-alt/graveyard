from django.conf.urls import patterns, include, url
from django.contrib import admin
from front import views
from registration.views import domain, contact, payment

urlpatterns = patterns(
    '',
    url(r'^$', views.Home.as_view(), name="home"),
    url(r'^registration/domain/$', domain, name="domain"),
    url(r'^registration/contact/$', contact, name="contact"),
    url(r'^registration/payment/$', payment, name="payment"),
    url(r'^admin/', include(admin.site.urls)),
)
