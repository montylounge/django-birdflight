from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "birdflight.views.homepage", name='home'),
    (r'^admin/(.*)', admin.site.root),
)
