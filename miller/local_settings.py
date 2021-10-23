#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
# | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
# | | ____    ____ | || |     _____    | || |   _____      | || |   _____      | || |  _________   | || |  _______     | |
# | ||_   \  /   _|| || |    |_   _|   | || |  |_   _|     | || |  |_   _|     | || | |_   ___  |  | || | |_   __ \    | |
# | |  |   \/   |  | || |      | |     | || |    | |       | || |    | |       | || |   | |_  \_|  | || |   | |__) |   | |
# | |  | |\  /| |  | || |      | |     | || |    | |   _   | || |    | |   _   | || |   |  _|  _   | || |   |  __ /    | |
# | | _| |_\/_| |_ | || |     _| |_    | || |   _| |__/ |  | || |   _| |__/ |  | || |  _| |___/ |  | || |  _| |  \ \_  | |
# | ||_____||_____|| || |    |_____|   | || |  |________|  | || |  |________|  | || | |_________|  | || | |____| |___| | |
# | |              | || |              | || |              | || |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
#  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
#
# """
# 1. MILLER own stuff.
# Please Provide translations for title and description.
# """
import os

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Debug javascript in template. Can be different from settings.DEBUG
MILLER_DEBUG = True

# will be used to send system emails (e.g account registration)
MILLER_EMAIL       = 'mt@mthomas-it.de'

# the html title?
MILLER_TITLE       = 'MILLER'

# html metadata description
MILLER_DESCRIPTION = '''
Long description'''

# the host, absolute without trailing slashes. Default: localhost for django debug
MILLER_DOMAIN_NAME   = 'localhost'
MILLER_HOST          = 'http://localhost:8000'
MILLER_HOST_PROTOCOL = 'http' # of https

# signature (unicode)
MILLER_SIGNEDBY    = u'The Editorial Team\nMiller – Université du Luxembourg\nWeb ' + MILLER_HOST

# the absolute path for websocket, absolute without trailing slashes. Default: localhost for django debug
MILLER_WS_HOST   = 'ws://localhost:8000/ws'

# the disqus id, if any
MILLER_DISQUS_ID = '***'

# twitter username associated with your account
MILLER_TWITTER_USERNAME = '***'
MILLER_TWITTER_SOCIALTAGS = ''


MILLER_FACEBOOK_APPID = None
# you can use this ref in your local_settings file
MILLER_TEMPLATE_BASE_DIR = '/home/mic/Projects/CELL/RESuME'

# (NOT YET IMPLEMENTED) Set to true and uncomment and fill the fields correctly
MILLER_FIREBASE_ENABLED = False
# MILLER_FIREBASE_APIKEY            = 'AIzaSyCC6ohIY_6Fe0VaaVGib5vEntSKJkvzyKM'
# MILLER_FIREBASE_AUTHDOMAIN        = 'resume-91a73.firebaseapp.com'
# MILLER_FIREBASE_DATABASEURL       = 'https://resume-91a73.firebaseio.com'
# MILLER_FIREBASE_STORAGEBUCKET     = 'resume-91a73.appspot.com'
# MILLER_FIREBASE_MESSAGINGSENDERID = '385835616038'

# CSV table for command task $ python manage.py task update_localisation and python manage.py task update_localisation_gs if you have a google spreadsheet table
MILLER_LOCALISATION_TABLE = os.path.join(MILLER_TEMPLATE_BASE_DIR, 'src/locale/locale-all.csv')
MILLER_LOCALISATION_TABLE_GOOGLE_SPREADSHEET = None

# Your Google Analytics account id.
MILLER_GA_ID = '******'

# OEMBED with noembed.
MILLER_EMBEDLY_API_KEY = '*****'
MILLER_IFRAMELY_API_KEY = None

# use this at your own sake.
MILLER_OEMBEDS = {
  'EMBEDLY_API_KEY': MILLER_EMBEDLY_API_KEY,
  'vimeo':  {
    'endpoint': 'https://vimeo.com/api/oembed.json'
  }
}

MILLER_REVIEW_DEFAULT_DUE_DATE_DAYS = 30


# """
# 2. Django registration app
# """
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 1025
EMAIL_ACTIVATION_ACCOUNT = MILLER_EMAIL

REGISTRATION_SALT = 'bibeIs1t'

DISABLE_EMAIL_ACTIVATION = True


RSS_TITLE = MILLER_TITLE # 
RSS_DESCRIPTION = MILLER_DESCRIPTION


# """
# 3. Go social, for django socual auth app.
# Identify Google, and choose your AUTHENTICATION_BACKENDS.
# """
GOOGLE_IDENTIFICATION = 'google650535b3d79acc59.html'


AUTHENTICATION_BACKENDS = (
  #'social.backends.google.GoogleOAuth2',
  #'social.backends.twitter.TwitterOAuth',
  'django.contrib.auth.backends.ModelBackend',
)

# SOCIAL_AUTH_TWITTER_KEY = '********'
# SOCIAL_AUTH_TWITTER_SECRET = '********'


# OCIAL_AUTH_GOOGLE_OAUTH2_KEY = '*******'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '**********'

# SOCIAL_AUTH_FACEBOOK_APPID = 'XXXYYYYZZZ'

SECRET_KEY = 'grd(u@re67qs*%4tm#xnws3)0t@k^=znp$1s!zex2eqabf7623'

# If you have one.
# SEO_JS_BACKEND = "django_seo_js.backends.PrerenderHosted"
# SEO_JS_PRERENDER_URL = "http://localhost:3000/"  # Note trailing slash.
# SEO_JS_PRERENDER_RECACHE_URL = "http://localhost:3000/recache"


ZOTERO_API_KEY = '******'
ZOTERO_IDENTITY = '******'
ZOTERO_BIB_FILE = 'zotero.bib'
ZOTERO_IDENTITY_NAME = 'miller'
SEO_JS_PRERENDER_TOKEN = 'abcdef'


# """
# 4. plain override settings.py
# Check MILLER_DOMAIN_NAME above
# """
DEBUG = True
ALLOWED_HOSTS = [MILLER_DOMAIN_NAME]
DEFAULT_FROM_EMAIL = MILLER_EMAIL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bibe',
        'USER': 'miller',
        'PASSWORD': 'miller',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# """
# 5. Templating
# Norlmally, you should not touch this. 
# Just fill MILLER_TEMPLATE_BASE_DIR above would suffice.
# """
# for debug purposes
STATIC_ROOT = os.path.join(MILLER_TEMPLATE_BASE_DIR, 'dist')
STATICFILES_DIRS = [
  '/home/mic/Projects/CELL/kc4s/src',
  os.path.join(MILLER_TEMPLATE_BASE_DIR, 'src'),
]

# templates. No need to extend this normally.
# Cfr. 'miller.context_processors.default'
# Should you need websocket support, put 'ws4redis.context_processors.default',
# before 'miller.context_processors.default'
TEMPLATES = [
  {
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': ['/home/mic/Projects/CELL/kc4s',MILLER_TEMPLATE_BASE_DIR, os.path.join(_BASE_DIR, 'miller', 'templates')],
      'APP_DIRS': True,
      'OPTIONS': {
          'context_processors': [
              'social.apps.django_app.context_processors.backends',
              'social.apps.django_app.context_processors.login_redirect',
              'django.template.context_processors.debug',
              'django.template.context_processors.request',
              'django.contrib.auth.context_processors.auth',
              # 'django.core.context_processors.static',
              'ws4redis.context_processors.default',
              'miller.context_processors.default',
              'django.contrib.messages.context_processors.messages',
          ],
      },
  },
]


# """
# 6. Flush in TEMPLATE. Check miller.context_processors.default
# Norlmally, you should not touch this. 
# """
# 
MILLER_SETTINGS = {
  'host': MILLER_HOST,
  'wshost': MILLER_WS_HOST,
  'debug': MILLER_DEBUG,
  'disqus': MILLER_DISQUS_ID,
  'analytics': MILLER_GA_ID,
  'facebook': MILLER_FACEBOOK_APPID,
  'twitter': {
    'username': MILLER_TWITTER_USERNAME,
    'socialtags': MILLER_TWITTER_SOCIALTAGS
  },
  'firebase': {
    'apiKey': MILLER_FIREBASE_APIKEY,
    'authDomain': MILLER_FIREBASE_AUTHDOMAIN,
    'databaseURL': MILLER_FIREBASE_DATABASEURL,
    'storageBucket': MILLER_FIREBASE_STORAGEBUCKET,
    'messagingSenderId': MILLER_FIREBASE_MESSAGINGSENDERID
  } if MILLER_FIREBASE_ENABLED else None
}
