from django import forms
from django.contrib.auth.models import User

class PostForm(forms.Form):
    question_title = forms.CharField(required=True)
    question_content = forms.CharField(required=True)

    class Meta:
        model = User

class PostViewForm(forms.Form):
	answer_content = forms.CharField(required=True)
	class Meta:
		model = User
