# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-16 03:22
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Birth_Date', models.DateField(blank=True, null=True)),
                ('Bio', models.TextField(blank=True, max_length=500)),
                ('Profile_Picture', models.ImageField(upload_to=b'')),
                ('Education_Level', models.CharField(choices=[('Some Highschool', 'Some Highschool'), ('Highschool', 'Highschool'), ('Some College', 'Some College'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Doctorate', 'Doctorate')], max_length=15, verbose_name='Education Level')),
                ('Education_Level_Priority', models.IntegerField(verbose_name='How important is Education Level?')),
                ('Institution', models.CharField(max_length=60)),
                ('Sponsorship', models.BooleanField()),
                ('Sponsorship_Priority', models.IntegerField(verbose_name='How important is Sponsorship?')),
                ('Skills', models.TextField(blank=True, verbose_name='Skills/Languages')),
                ('Skills_Priority', models.IntegerField(verbose_name='How important is(are) Skills?')),
                ('Industry', models.CharField(choices=[('Technology', 'Technology'), ('Health', 'Health'), ('Finance', 'Finance'), ('Education', 'Education'), ('Retail', 'Retail'), ('Fashion', 'Fashion')], max_length=20)),
                ('Industry_Priority', models.IntegerField(verbose_name='How important is Industry?')),
                ('Location', models.CharField(choices=[('West Coast', 'West Coast'), ('East Coast', 'East Coast'), ('Midwest', 'Midwest'), ('South', 'South'), ('International', 'International')], max_length=20)),
                ('Location_Priority', models.IntegerField(verbose_name='How important is Location?')),
                ('isSeeker', models.NullBooleanField()),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
