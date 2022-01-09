import re
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from markdown import markdown
from markdown.extensions import Extension
from markdown.extensions.toc import TocExtension


register = template.Library()

class MagicLinks(Extension):
  def extendMarkdown(self, md, md_globals):
    pass
    #print 'exted!!!!!!!!!!!', md.inlinePatterns['link']

@register.simple_tag()
def publication_title():
  return settings.MILLER_TITLE


@register.simple_tag()
def lookup(obj, path, language):
  desiredLanguage = [item[2] for item in settings.LANGUAGES if item[0] == language][0]
  defaultLanguage = [item[2] for item in settings.LANGUAGES if item[0] == settings.LANGUAGE_CODE][0]

  contents = obj.get(path, {})

  if isinstance(contents, basestring):
    return contents

  if desiredLanguage in contents:
    return contents.get(desiredLanguage, '')
  if defaultLanguage in contents:
    return contents.get(defaultLanguage)

  keys = list(contents)
  if not keys:
    return ''
  return contents.get(keys[0], '')


@register.simple_tag()
def lookupmulti(obj, key, language, html=False):
    """
    Lookup in single translation json file for simplicity sake
    usage: ?

    """
    languageKey = [item[2] for item in settings.LANGUAGES if language in item[0]][0]
    print "languageKey = " + languageKey
    defaultLanguageKey = [item[2] for item in settings.LANGUAGES if item[0] == settings.LANGUAGE_CODE][0]
    print "defaultLanguageKey = " + defaultLanguageKey

    # get language if any
    content = obj.get(languageKey, {}).get(key, None)
    if content is not None:
        return mark_safe(markdown(content, extensions=['markdown.extensions.nl2br'])) if html else content

    # get default language if any
    content = obj.get(defaultLanguageKey, {}).get(key, None)
    if content is not None:
        return mark_safe(markdown(content, extensions=['markdown.extensions.nl2br'])) if html else content
    return key


@register.simple_tag()
def signedby(html=False):
  text = settings.MILLER_SIGNEDBY
  return mark_safe(markdown(text, extensions=['markdown.extensions.nl2br'])) if html else text

@register.simple_tag()
def htmlsignedby():
  return signedby(html=True)



@register.simple_tag()
def markdownit(text, language):
  if not text:
    return ''

  desiredLanguage = [item[2] for item in settings.LANGUAGES if item[0] == language][0]
  defaultLanguage = [item[2] for item in settings.LANGUAGES if item[0] == settings.LANGUAGE_CODE][0]

  candidates = filter(None, re.split(r'<!--\s*(lang:[a-zA-Z_]{2,5})\s*-->', text))

  # print (zip(candidate, candidate))
  # candidate.length should be a multiple of 2
  if len(candidates) % 2 == 0:
    d  = {k:v for k,v in zip(*[iter(candidates)]*2)}
    k  = 'lang:%s' % desiredLanguage
    dk = 'lang:%s' % defaultLanguage
    if k in d:
      text = d[k]
    elif dk in d:
      text = d[dk]
    else:
      text = d.itervalues().next()


  return mark_safe(markdown(text, extensions=['footnotes', TocExtension(baselevel=2), MagicLinks()]))


@register.filter()
def coverage(cover):
  url = None

  if cover.snapshot:
    return '/'.join(s.strip('/') for s in [
      settings.MILLER_SETTINGS['host'],
      cover.snapshot.url
    ])

  url = cover.data['thumbnail_url'] if 'thumbnail_url' in cover.data else None
  if not url:
    url = cover.dmetadata['preview'] if 'preview' in cover.data else None
  if not url:
    url = cover.snapshot if cover.snapshot else cover.attachment
  if not url:
    url = cover.data['media_url'] if 'media_ur' in cover.data else None

  if not url:
    url = cover.data['url'] if 'url' in cover.data else None
    # || cover.metadata.preview || _.get(cover, 'metadata.urls.Preview')  || cover.snapshot || cover.attachment || cover.metadata.url;
  if not url:
    url = cover.snapshot if cover.snapshot else cover.attachment

  ## prefix (media_url) if not an absolute url


  return url;


@register.filter()
def urled(url):
  return url.replace('accessibility/', '')


@register.simple_tag()
def qsfilter(qs, key, value):
  return qs.filter(**{key:value})


@register.filter()
def shorten(text, maxwords=5):
  if not text:
    return '';
  words = re.split(r'(?!=\.\s)\s', text)[:maxwords];

  sentence = ' '.join(words)

  if len(sentence) < len(text):
    # if(!sentence.match(/\?\!\.$/)){
    #   sentence += ' '
    # }

    sentence = '%s ...' % sentence
  return sentence;
