from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^', include('webfolder.webfolder.urls')),
                       # Examples:
                       # url(r'^$', 'webui.views.home', name='home'),
                       # url(r'^webui/', include('webui.foo.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
                       )
