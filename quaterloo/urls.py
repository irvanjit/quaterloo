from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from auth.views import LandingView
from posts.views import HomeView, PostView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

	#TEST
    url(r'^about/', 'auth.views.hello'),
    url(r'^stats/', 'stats.views.stats'),
    url(r'^info/', 'auth.views.info'),

    #CAS
    url(r'^accounts/login/$', 'cas.views.login', name='login'),
    url(r'^accounts/logout/$', 'cas.views.logout', name='logout'),

    #APP
    url(r'^$', LandingView.as_view(), name='login'),
    url(r'^home/?$', login_required(HomeView.as_view()), name='home'),
    #post urls
    url(r'^posts/(?P<post_id>\d+)/?$', login_required(PostView.as_view()), name='post_view')
)
