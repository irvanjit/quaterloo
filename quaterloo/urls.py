from django.conf.urls import patterns, include, url
from django.contrib import admin

from auth.views import LandingView
from posts.views import HomeView, PostView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

	#TEST
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'auth.views.hello'),
    url(r'^test/', 'auth.views.test'),

    #CAS
    url(r'^login/$', 'cas.views.login', name='login'),
    url(r'^logout/$', 'cas.views.logout', name='logout'),

    #
    url(r'^$', LandingView.as_view(), name='login'),
    url(r'^home/?$', HomeView.as_view(), name='home'),
    #post urls
    url(r'^posts/(?P<post_id>\d+)/?$', PostView.as_view(), name='post_view')
)
