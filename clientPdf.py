import urllib.request
import urllib.parse
import hashlib

def generate_pdf_api_url(customer_key, secret_phrase, options):
  api_url = 'https://pdfapi.screenshotmachine.com/?key=' + customer_key
  if secret_phrase:
    api_url = api_url + '&hash=' + hashlib.md5((options.get('url') + secret_phrase).encode('utf-8')).hexdigest()
  api_url = api_url + '&' + urllib.parse.urlencode(options)
  return api_url;


customer_key = 'PUT_YOUR_CUSTOMER_KEY_HERE'
secret_phrase = '' # leave secret phrase empty, if not needed
options = {
  'url': 'https://www.google.com', # mandatory parameter
  # all next parameters are optional, see our website to PDF API guide for more details
  'paper': 'letter',
  'orientation': 'portrait',
  'media': 'print',
  'bg' : 'nobg',
  'delay' : '2000',
  'scale' : '50'
}

pdf_api_url = generate_pdf_api_url(customer_key, secret_phrase, options)

#save PDF file
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', '-')]
urllib.request.install_opener(opener)
output = 'output.pdf'
urllib.request.urlretrieve(pdf_api_url, output)
print('PDF saved as ' + output);
