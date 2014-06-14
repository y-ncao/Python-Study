#!/usr/bin/env python
"""
import urllib
import urllib2

response = urllib2.urlopen('http://python.org/')
html = response.read()
f = open('test.html', 'w')
f.write(html)
f.close

url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }

data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
"""
import requests

#r = requests.get('https://github.com/timeline.json')
#print r
headers = {
"Authorization: OAuth oauth_consumer_key":"J1IBcJEkNPI1m0fzhW97HyRmi", "oauth_nonce":"9b55cd75065570c5ad2b514e68575688", "oauth_signature":"3I%2FyJsgaWC6zIKtbGF3eF%2BuWTes%3D", "oauth_signature_method":"HMAC-SHA1", "oauth_timestamp":"1402635265", "oauth_token":"", "oauth_version":"1.0"}

r = requests.get('https://api.twitter.com/1.1/', headers=headers)
print r
