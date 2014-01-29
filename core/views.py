from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson as json
from django.core.urlresolvers import reverse
from models import Question, Answer, Comment
from operator import attrgetter
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response

import forms
from django.core.exceptions import ValidationError


class AboutView(APIView):
    template = 'about.html'
    def get(self, request, *args, **kwargs):
        context = RequestContext(request)
        return render_to_response(self.template, context_instance=context)


class HomeView(APIView):
    template = 'home.html'

    def get(self, request, *args, **kwargs):
        questions = sorted(Question.objects.all(), key=attrgetter('id'), reverse=True)
        context = RequestContext(request, {'questions': questions})
        return render_to_response(self.template, context_instance=context)

    def post(self, request, *args, **kwargs):
        form = forms.PostForm(request.POST)
        try:
            if(form.is_valid()):
                title = request.POST.get('question_title', '')
                question = Question(user=request.user, title=request.POST.get('question_title', ''), content=request.POST.get('question_content', ''))
                question.save()
                return HttpResponseRedirect("")
            questions = sorted(Question.objects.all(), key=attrgetter('id'), reverse=True)
            context = RequestContext(request, {'first_name': request.user.username, 'questions': questions})
            return render_to_response(self.template, context_instance=context)

        except ValidationError as v:
            return HttpResponseBadRequest(json.dumps(v.mesage_dict))
        except Exception as e:
            return HttpResponseBadRequest(json.dumps({'error': e.message}))


class PostView(APIView):
    template = 'post.html'

    def get(self, request, *args, **kwargs):
        try:
            question = Question.objects.get(id=int(kwargs['post_id']))
            answers = sorted(Answer.objects.filter(question=question), key=attrgetter('id'))
            context = RequestContext(request, {'question': question, 'answers': answers})
            return render_to_response(self.template, context_instance=context)
        except Question.DoesNotExist as e:
            return Response(400, e.message)
        except KeyError:
            context = RequestContext(request, {'new_post': 'YES'})
            return render_to_response(self.template, context_instance=context)

    def post(self, request, *args, **kwargs):
        form = forms.PostViewForm(request.POST)
        try:
            if(form.is_valid()):
                post_id = kwargs['post_id']
                q = Question.objects.get(id=post_id)
                answer = Answer(user=request.user, question=q, content=request.POST.get('answer_content', ''))
                answer.save()
                return HttpResponseRedirect("/posts/" + post_id)
            answers = sorted(Answer.objects.filter(question=q), key=attrgetter('id'))
            # views.create(title)
            context = RequestContext(request, {'first_name': request.user.username, 'question':q, 'answers': answers})
            return render_to_response(self.template, context_instance=context)

        except ValidationError as v:
            return HttpResponseBadRequest(json.dumps(v.mesage_dict))
        except Exception as e:
            return HttpResponseBadRequest(json.dumps({'error': e.message}))
