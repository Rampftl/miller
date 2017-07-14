import requests, logging, re

from django.conf import settings
from requests.exceptions import ConnectionError, HTTPError
from rest_framework.exceptions import ValidationError, AuthenticationFailed


logger = logging.getLogger('miller.doi')

def urlize(*args):
    return '/'.join(s.strip('/') for s in filter(lambda x: isinstance(x, basestring), args))


class DataciteDOI():
  prefix    = settings.MILLER_DOI_PREFIX
  publisher = settings.MILLER_DOI_PUBLISHER
  endpoint  = urlize(settings.MILLER_DOI_ENDPOINT, 'doi')
  auth      = settings.MILLER_DOI_AUTH
  baseurl   = '/'.join(s.strip('/') for s in (settings.MILLER_HOST, 'doi')) 

  def __init__(self, story):
    self.story   = story
    self.id      = None
    self._id     = self.format()
    self._url = urlize(self.baseurl, self._id)
    


  def config(self):
    return {
      'enabled': settings.MILLER_DOI_ENABLED,
      'baseurl': self.baseurl,
      
      'endpoint':    self.endpoint,
      'publisher':    self.publisher,
      'prefix': self.prefix
    }

  def format(self):
    return urlize(self.prefix, '%s-%s' % (self.story.short_url, self.story.date.year))

  @staticmethod
  
  def list(self):
    pass

  def _log_prefix(self):
    return 'doi {_id: %s, id:%s}' % (self._id, self.id)

  def create(self):
    """
    Return a doi representation, if any was created. 
    Raise exception otherwise.
    """
    logger.debug('%s'%self._log_prefix())

    data = u'#Content-Type:text/plain;charset=UTF-8\ndoi= %s\nurl= http://example.org/' % self._id
    logger.debug(data)
    res = self.perform_request(path=self._id, method='put', data={
      'doi': self._id,
      'url': self._url
    }, headers={
      "Content-Type":"text/plain;charset=UTF-8"
    })

    print res.text
    return res


  def retrieve(self):

    pass

  def perform_request(self, data=None, method='get', headers=None, path=None):
    """
    Perform request against dooi api endpoint and raise REST Framework exceptions
    """
    if not settings.MILLER_DOI_ENABLED:
      raise ParseError({
        'error': 'check settings.MILLER_DOI_ENABLED' % e
      })
    url = urlize(self.endpoint, path)
    #logger.debug('%s: %s %s' % (self._log_prefix(), method.upper(), url))
    

    try:
      
      res = getattr(requests, method.lower())(url=url, data=data, auth=self.auth, headers=headers)
    except ConnectionError as e:
      logger.exception(e)
      raise e
    else:
      logger.debug('%s: %s %s received %s' % (self._log_prefix(), method.upper(), url, res.status_code))

    try:
      res.raise_for_status()
    except HTTPError as e:
      if res.status_code == 401:
        raise AuthenticationFailed({
          'details': 'unable to authenticate against `datacite.org` DOI service',
          'config': self.config()
        })
      elif res.status_code == 400:
        
        raise ValidationError({
            'error': res.text,
            'value': data,
            'endpoint': url
          })
      else:
        logger.exception(e)
        raise e
    
    return res



class DataciteDOIMetadata(DataciteDOI):
  endpoint  = urlize(settings.MILLER_DOI_ENDPOINT, 'metadata')

  def serialize(self):
    """
    Return a serialized version of the dictionary given
    """
    xml = u"""
        <?xml version="1.0" encoding="UTF-8"?>
      <resource xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://datacite.org/schema/kernel-4" xsi:schemaLocation="http://datacite.org/schema/kernel-4 http://schema.datacite.org/meta/kernel-4/metadata.xsd">
        <identifier identifierType="DOI">%(DOI)s</identifier>
        <creators>%(creators)s</creators>
        <titles>
          <title>%(title)s</title>
        </titles>
        <publisher>%(publisher)s</publisher>
        <publicationYear>%(publicationYear)s</publicationYear>
        <resourceType resourceTypeGeneral="%(resourceTypeGeneral)s">%(resourceType)s</resourceType>
        <dates/>
        <descriptions><description descriptionType="Abstract">%(abstract)s</description></descriptions>
      </resource> """ % {
        'DOI': self._id,
        'creators': u''.join([author.asXMLCreator() for author in self.story.authors.all()]),
        'title': self.story.title,
        'publisher': self.publisher,
        'publicationYear': '%s' % self.story.date.year,
        'resourceTypeGeneral': 'Text',
        'resourceType': 'article',
        'abstract': self.story.abstract
      }

    return re.sub(r'\n\s+','', xml.strip().encode('utf-8'))


  def create(self):
    """
    Send an xml representing the metadata
    """
    
    res = self.perform_request(data=self.serialize(), headers={
      'Content-Type': 'application/xml',
      'charset': 'UTF-8'
    }, method='POST')
    return res.text

  def retrieve(self):
    """
    Retrieve XML metadata.
    """
    res = self.perform_request(path=self._id, headers={
      'Content-Type': 'application/xml',
      'charset': 'UTF-8'
    }, method='GET')
    return res.text
