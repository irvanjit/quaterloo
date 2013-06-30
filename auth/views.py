from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.generic.base import View
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils import simplejson as json
from django.db.transaction import commit_on_success
from django.views.generic.edit import FormView

def hello(request):
	return HttpResponse('hello world!')


@login_required
def test(request):
	return HttpResponse('auth page')

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')

@login_required
def home(request):
    template = 'home.html'
    user = request.user
    context = {'first_name': user.username}
    return render_to_response(template, context)


class LandingView(View):
    template = 'login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home'))
        context = {}
        return render(request, self.template, context)
