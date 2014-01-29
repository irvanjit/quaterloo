from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from auth.views import LandingView
from core.views import AboutView, HomeView, PostView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

	#


    #CAS
    url(r'^accounts/login/$', 'cas.views.login', name='login'),
    url(r'^accounts/logout/$', 'cas.views.logout', name='logout'),

    #OTHER LOGIN
    # url(r'^alt_login/$','auth.views.alt_login', name='alt_login'),

    #APP
    url(r'^$', LandingView.as_view(), name='login'),
    url(r'^home/?$', login_required(HomeView.as_view()), name='home'),
    url(r'^about/?$', AboutView.as_view(), name='about'),
    #post urls
    url(r'^posts/new/?$', login_required(PostView.as_view()), name='post_view'),
    url(r'^posts/(?P<post_id>\d+)/?$', login_required(PostView.as_view()), name='post_view')
)
