import requests

resp = requests.get("https://httpbin.org/get")
print(resp.content)

r_data = 'Request data'
resp = requests.post(url = "https://httpbin.org/post",
                           data = r_data,
                     headers={'h1':'Our Header 1'})
print('POST status', resp.status_code)
print(resp.content)
