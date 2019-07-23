# screenshotmachine-python

This demo shows how to call online screenshot machine' API using python3.

## Installation
First, you need to create a free/premium account at [www.screenshotmachine.com](https://www.screenshotmachine.com) website. After registration, you will see your customer key in your user profile. Also secret phrase is maintained here. Please, use secret phrase always, when your API calls are called from publicly available websites.  

Set-up your customer key and secret phrase (if needed) in the script:

```python
customer_key = 'PUT_YOUR_CUSTOMER_KEY_HERE'
secret_phrase = '' # leave secret phrase empty, if not needed
```

Set other options to fulfill your needs: 

```python
options = {
  'url': 'https://www.google.com', # mandatory parameter
  # all next parameters are optional, see our API guide for more details
  'dimension': '1366x768', # or "1366xfull" for full length screenshot
  'device': 'desktop',
  'cacheLimit' : '0',
  'delay' : '200'
  }
```
More info about options can be found in our [API guide](https://www.screenshotmachine.com/apiguide.php).  

 Sample code
-----

```python
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
```
Generated ```api_url```  link can be placed in ```<img>``` tag or used in your business logic later.

If you need to store captured screenshot as an image, just call:

```python
api_url = generate_api_url(customer_key, secret_phrase, options)

#save screenshot as an image
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', '-')]
urllib.request.install_opener(opener)
output = 'output.png'
urllib.request.urlretrieve(api_url, output)
print('Screenshot saved as ' + output);
```


Captured screenshot will be saved as ```output.png``` file in current directory.

# License

The MIT License (MIT)    