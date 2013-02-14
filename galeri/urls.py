from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('galeri.views',
    # Examples:
    # url(r'^$', 'useder.views.home', name='home'),
    # url(r'^useder/', include('useder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', 'index'),
    url(r'^(?P<album_id>\d+)/$', 'album'),

   

)
