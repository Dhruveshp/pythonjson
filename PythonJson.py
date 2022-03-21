import requests
country = 'Puerto Rico'
phonenumber = '564593986'
lists = []
lists2 = []

apiRequest = requests.get('https://jsonmock.hackerrank.com/api/countries?name='+str(country))
articles = apiRequest.json()['data']

for i in articles:
    value = i['name']
    if value == country:
        x = i['callingCodes']
        for k in range(0, len(x)):
            lists.append(int(x[k]))

for k in range(0, len(lists)):
    lists2.append(int(lists[k]))

print(lists2)
