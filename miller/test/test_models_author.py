#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from miller import helpers
from miller.models import Document, Author


dir_path = os.path.dirname(os.path.realpath(__file__))

# python manage.py test miller.test.test_models_author.AuthorTest
class AuthorTest(TestCase):

  def setUp(self):
    self.user = User.objects.create_user(
        username='jacob-generic', 
        first_name='Jacob',
        last_name='Generic',
        email='jacob@jacob', 
        password='top_secret')


  def test_creation(self):
    self.assertEqual(self.user.authorship.all()[0].fullname, 'Jacob Generic')
    self.assertEqual(self.user.authorship.all()[0].slug, 'jacob-generic')

    autOm = Author(user=self.user, fullname='jacob generic')
    autOm.save()

    self.assertEqual(self.user.authorship.count(), 2)
    self.assertEqual(self.user.authorship.all()[1].slug, 'jacob-generic-1')
    