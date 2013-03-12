from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# Para los archivos estaticos
urlpatterns += staticfiles_urlpatterns()

# Urls del blog
urlpatterns += patterns('blog.views',
	# La url para accesar al blog Cargara en el index
	url(r'^$', 'index'),
	# individual post
	url(r'^(?P<id>[\d]+)/(?P<slug>[-\w]+)/$', 'view_post'),
)

