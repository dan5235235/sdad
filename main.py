import urllib.request as ur
print('HTTP Request')
print('https://httpbin.org/get')

opener = ur.build_opener()
resp = opener.open("https://httpbin.org/get")


#for _ in resp.read():
#    print(_)


print(resp.read())