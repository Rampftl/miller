#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from registration.forms import RegistrationFormUniqueEmail

class LoginForm(forms.Form):
  username = forms.CharField(max_length=128, widget=forms.TextInput)
  password = forms.CharField(max_length=64, label='Password', widget=forms.PasswordInput(render_value=False))

class SearchQueryForm(forms.Form):
  q = forms.CharField(max_length=128, widget=forms.TextInput, required=False)
  tags = forms.CharField(max_length=128, required=False)
  authors = forms.CharField(max_length=128, required=False)

class UploadDocxForm(forms.Form):
  docx = forms.FileField()


class SignupForm(RegistrationFormUniqueEmail):
  captcha     = CaptchaField()

  tos         = forms.BooleanField(widget=forms.CheckboxInput)

  first_name  = forms.CharField(min_length=3, max_length=128, widget=forms.TextInput)
  last_name   = forms.CharField(min_length=3, max_length=128, widget=forms.TextInput)
  affiliation = forms.CharField(required=False, max_length=500, widget=forms.TextInput)