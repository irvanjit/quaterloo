from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# class UserProfile(models.Model):
# 	user = models.ForeignKey(User, unique=True)
# 	school = models.CharField(max_length=200, null=True)
# 	faculty = models.CharField(max_length=200, null=True)
# 	program = models.CharField(max_length=400, null=True)
# 	year = models.CharField(max_length=200, null=True)


# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		UserProfile.objects.create(user=instance)

# post_save.connect(create_user_profile, sender=User)