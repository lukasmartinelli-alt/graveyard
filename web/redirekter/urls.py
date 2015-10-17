from django.conf.urls import include, url
from django.contrib import admin

from .apps.reviews import views as review_views

urlpatterns = [
    url(r'^$', review_views.home),
    url(r'^logout/$', review_views.logout),
    url(r'^reviews/$', review_views.browse, name='browse'),
    url(r'^reviews/new/$', review_views.new, name='new'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
