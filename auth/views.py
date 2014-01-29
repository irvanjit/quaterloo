from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.views.generic.base import View
from django.template import RequestContext
from django.utils import simplejson as json
from django.db.transaction import commit_on_success
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate
# from auth.models import UserProfile


# @login_required
# def info(request):
#     if request.method == 'POST':
#         info = request.POST
#         profile = request.user.get_profile()
#         pdb.set_trace()
#         if info.get('faculty') is not None:
#             profile.faculty = info.get('faculty')
#         if info.get('year') is not None:
#             profile.year = info.get('year')
#         school = 'University of Waterloo'
#         profile.school = school
#         profile.save()
#     return HttpResponseRedirect(reverse('home'))
#     else:
#         context = RequestContext(request)
#         return render_to_response('info_form.html', context_instance=context)


# def alt_login(request, *args, **kwargs):
#     uid = request.GET.get('id')
#     passphrase = request.GET.get('pass')
#     pdb.set_trace()
#     if (uid == 'uw' and passphrase == 'uw'):
#         pdb.set_trace()
#         user = authenticate(username='guest', password='guestpass')
#         template = 'alt_login.html'
#         return render_to_response(template)
#     return HttpResponse('bad login')

# @login_required
# def logout(request):
#     logout(request)
#     return HttpResponseRedirect('/')

class LandingView(View):
    template = 'login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            # profile = request.user.get_profile()
            # if profile.school is not None:
            return HttpResponseRedirect(reverse('home'))
            # else:
            #     return HttpResponseRedirect('info')
        context = {}
        return render(request, self.template, context)
