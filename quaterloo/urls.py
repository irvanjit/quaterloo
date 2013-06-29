from django.conf.urls import patterns, include, url
from django.contrib import admin

from auth.views import LandingView, logout, RegistrationView
from posts.views import HomeView, PostView

admin.autodiscover()

urlpatterns = patterns('',
	#TEST
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'auth.views.hello'),
    url(r'^test/', 'auth.views.test'),

    # CAS
    url(r'^accounts/login/$', 'cas.views.login'),
    url(r'^accounts/logout/$', 'cas.views.logout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LandingView.as_view(), name='login'),
    url(r'^logout/?$', logout, name='logout'),
    url(r'^home/?$', HomeView.as_view(), name='home'),
    url(r'^register/?$', RegistrationView.as_view(), name='register'),
    #post urls
    url(r'^posts/(?P<post_id>\d+)/?$', PostView.as_view(), name='post_view')
)
