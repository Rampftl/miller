"""miller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps import views as sitemaps_views
from django.views.generic import TemplateView
from django.views.i18n import set_language

from rest_framework import routers

from miller import views, services, api
from miller.feeds import LatestEntriesFeed, AtomLatestEntriesFeed
from miller.sitemaps import sitemaps
from miller.views import _share
#from miller.forms import SignupForm
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter(trailing_slash=True)

router.register(r'user', api.UserViewSet)
router.register(r'collection', api.CollectionViewSet)
router.register(r'story', api.StoryViewSet)
router.register(r'caption', api.CaptionViewSet)
router.register(r'document', api.DocumentViewSet)
router.register(r'mention', api.MentionViewSet)
router.register(r'profile', api.ProfileViewSet)
router.register(r'tag', api.TagViewSet)
router.register(r'comment', api.CommentViewSet)
router.register(r'author', api.AuthorViewSet)
router.register(r'review', api.ReviewViewSet)
router.register(r'pulse', api.PulseViewSet)
router.register(r'page', api.PageViewSet)



urlpatterns = [
  url(r'^$', views.home, name='home'),
  url(r'^admin/', admin.site.urls),

  url(r'^sitemap\.xml$', sitemaps_views.index, {'sitemaps': sitemaps}),
  url(r'^sitemap-(?P<section>.+)\.xml$', sitemaps_views.sitemap, {'sitemaps': sitemaps, 'template_name': 'sitemaps/sitemap.section.html'},
    name='django.contrib.sitemaps.views.sitemap'),

  url(r'^api/', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls')),

  # missing images service (e.g.crop)
  url(r'^services/images', services.images),

  url(r'^timelinejs/(?P<gsid>[A-Za-z0-9\-_]+)$', views.timelinejs), #iframe for timelinejs, given a google spreadsheet id so that we can use our own style.

  url(r'^login/$', auth_views.login, {'template_name': 'miller/login.html'}, name='login_view'), # views.login_view, name='login_view'),
  # url(r'^login/$', views.login_view, name='login_view'),

  url(r'^signup/$', views.signup_view, name='signup_view'),


  url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout_view'),
  url(r'^social/', include('social.apps.django_app.urls', namespace='social')),

  url(r'^contact-us-de_DE/$', views.contact_view,  {'lang': 'de'}, name='contact_view'),
  url(r'^contact-us-en_US/$', views.contact_view,  {'lang': 'en'}, name='contact_view'),
  url(r'^contact-us-fr_FR/$', views.contact_view,  {'lang': 'fr'}, name='contact_view'),

  url(r'^latest/rss\.xml$', LatestEntriesFeed(), name='latest_rss'),
  url(r'^latest/atom/$', AtomLatestEntriesFeed()),

  url(r'^auth/', include('djoser.urls.authtoken')),
  url(r'^captcha/', include('captcha.urls')),
  url(r'^accounts/activate/complete/', views.activation_complete, name='activation_complete'),
  url(r'^accounts/', include('registration.backends.hmac.urls')),

  url(r'^', include('templated_email.urls', namespace='templated_email')),
]

if hasattr(settings, 'GOOGLE_IDENTIFICATION'):
  urlpatterns = urlpatterns + [
    url(r'^'+ settings.GOOGLE_IDENTIFICATION + r'$', TemplateView.as_view(template_name=settings.GOOGLE_IDENTIFICATION)),
    url(r'^accessibility/$' + settings.GOOGLE_IDENTIFICATION + r'$', TemplateView.as_view(template_name=settings.GOOGLE_IDENTIFICATION)),
  ]

# redirect everything here
urlpatterns = urlpatterns + [
  url(r'^setlang/', set_language, name="setlang"),

  url(r'^accessibility$', views.accessibility_index, name='accessibility_index'),
  url(r'^accessibility/$', views.accessibility_index, name='accessibility_index_with_slash'),
  url(r'^accessibility/publications$', views.accessibility_stories, name='accessibility_stories'),
  url(r'^accessibility/publications/(?P<tag>[A-Za-z\-]+)$', views.accessibility_stories, name='accessibility_stories'),
  url(r'^accessibility/story/(?P<pk>[A-Za-z0-9\-]+)$', views.accessibility_story, name='accessibility_story'),
  url(r'^accessibility/collection/(?P<pk>[A-Za-z0-9\-]+)$', views.accessibility_collection, name='accessibility_collection'),
  url(r'^accessibility/author/(?P<author>[A-Za-z0-9\-]+)/publications$', views.accessibility_author, name='accessibility_author'),

  # sitemaps for search engines...
  url(r'^accessibility/sitemap\.xml$', sitemaps_views.index, {'sitemaps': sitemaps, 'template_name': 'sitemaps/sitemap.html'}),
  url(r'^accessibility/sitemap-(?P<section>.+)\.xml$', sitemaps_views.sitemap, {'sitemaps': sitemaps, 'template_name': 'sitemaps/sitemap.section.html'},
    name='django.contrib.sitemaps.views.sitemap'),

  # doi access (redirection) for search engine.
  url(r'^accessibility/doi/(?P<prefix>[\d\.A-Za-z\-]+)/(?P<short_url>[A-Za-z\d]+)-(?P<publication_year>\d+)$', views.accessibility_doi, name='accessibility_doi'),

  url(r'^accessibility/(?P<page>[A-Za-z\-]+)$', views.accessibility_page, name='accessibility_page'),




  # oaht2 toolkit here
  url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),


  # url(r'^(?!(login|logout)).*$', views.home, name='app'),
  url(r'^(?!favicon\.ico|api/|admin/|signup|media).*$', views.home, name='app')
]


if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
