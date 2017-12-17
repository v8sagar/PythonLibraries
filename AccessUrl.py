import urllib.request


urlRequest = urllib.request.urlopen('https://www.google.com')

print(urlRequest.read())