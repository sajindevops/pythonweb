from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import ugettext_lazy as _
import uuid
import datetime


class Cluster_admin(models.Model):
	user_id   			= models.AutoField(primary_key = True)
	user_name 			= models.CharField(max_length = 100)
	user_password 		= models.CharField(max_length = 50)

	class Meta:
		ordering = ['user_name']

	def __str__(self):
		return self.user_name