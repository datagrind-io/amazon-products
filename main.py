import urllib.request

response = urllib.request.urlopen('https://httpbin.org/uuid')
data = response.read()
output = data.decode('utf-8')
print(output)
