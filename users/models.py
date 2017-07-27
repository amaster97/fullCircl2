# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.

EDUCATION_LEVELS = (
	('Some Highschool', 'Some Highschool'),
	('Highschool', 'Highschool'),
	('Some College', 'Some College'),
	('Bachelors', 'Bachelors'),
	('Masters', 'Masters'),
	('Doctorate', 'Doctorate')
)

INDUSTRIES = (
	('Technology', 'Technology'),
	('Health', 'Health'),
	('Finance', 'Finance'),
	('Education', 'Education'),
	('Retail', 'Retail'),
	('Fashion', 'Fashion'),
)

REGIONS = (
	('West Coast', 'West Coast'),
	('East Coast', 'East Coast'),
	('Midwest', 'Midwest'),
	('South', 'South'),
	('International', 'International'),
)

class User(AbstractUser):
	Birth_Date = models.DateField(null=True, blank=True)

	Bio = models.TextField(max_length=500, blank=True)
	Profile_Picture = models.ImageField()
	
	Education_Level = models.CharField(max_length=15, choices=EDUCATION_LEVELS, verbose_name='Education Level')
	Education_Level_Priority = models.IntegerField(verbose_name='How important is Education Level?')
	Institution = models.CharField(max_length=60)
	
	Sponsorship = models.BooleanField(blank=True)
	Sponsorship_Priority = models.IntegerField(verbose_name='How important is Sponsorship?')
	
	Skills = models.TextField(blank=True, verbose_name='Skills/Languages')
	Skills_Priority = models.IntegerField(verbose_name='How important is(are) Skills?')
	
	Industry = models.CharField(max_length=20, choices=INDUSTRIES)
	Industry_Priority = models.IntegerField(verbose_name='How important is Industry?')
	
	Location = models.CharField(max_length=20, choices=REGIONS)
	Location_Priority = models.IntegerField(verbose_name='How important is Location?')
	
	isSeeker = models.NullBooleanField()

