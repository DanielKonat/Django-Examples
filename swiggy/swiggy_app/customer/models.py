# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
	name=models.CharField(max_length=255)
	description=models.TextField()
	enabled=models.BooleanField()
	price=models.FloatField()