import requests

response = requests.get('https://coinmarketcap.com/')
#print(response.content)
list_courses = []
list_tags = response.text.split('<span>')
for span in list_tags:
    if span.startswith('$'):
        for span_part in span.split('</span>'):
            if span_part.startswith('$'):
                list_courses.append(span_part)


print('Coin course: ', list_courses[0])

