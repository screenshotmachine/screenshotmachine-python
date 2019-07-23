import urllib.request
import urllib.parse
import hashlib

def generate_api_url(customer_key, secret_phrase, options):
  api_url = 'https://api.screenshotmachine.com/?key=' + customer_key
  if secret_phrase:
    api_url = api_url + '&hash=' + hashlib.md5((options.get('url') + secret_phrase).encode('utf-8')).hexdigest()
  api_url = api_url + '&' + urllib.parse.urlencode(options)
  return api_url;


customer_key = 'PUT_YOUR_CUSTOMER_KEY_HERE'
secret_phrase = '' # leave secret phrase empty, if not needed
options = {
  'url': 'https://www.google.com', # mandatory parameter
  # all next parameters are optional, see our API guide for more details
  'dimension': '1366x768', # or "1366xfull" for full length screenshot
  'device': 'desktop',
  'cacheLimit' : '0',
  'delay' : '200'
  }

api_url = generate_api_url(customer_key, secret_phrase, options)

#put link to your html code
print('<img src="'  + api_url + '">')

#or save screenshot as an image
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', '-')]
urllib.request.install_opener(opener)
output = 'output.png'
urllib.request.urlretrieve(api_url, output)
print('Screenshot saved as ' + output);
