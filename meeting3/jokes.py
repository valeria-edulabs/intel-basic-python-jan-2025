import pprint

import requests

# https://api.chucknorris.io/jokes/random
# https://api.chucknorris.io/jokes/categories
# https://api.chucknorris.io/jokes/random?category={category}
# https://api.chucknorris.io/jokes/search?query={query}

# response = requests.get("https://api.chucknorris.io/jokes/random")
# print(response.status_code)
# if response.status_code == 200:
#     data = response.text
#     print(type(data))
#     data = response.json()
#     print(data['value'])
# response = requests.get("https://api.chucknorris.io/jokes/randommmm")
# print(response.status_code)


params = {
    "query": "eat"
}
response = requests.get("https://api.chucknorris.io/jokes/search", params)
print(response.status_code)
pprint.pprint(response.json())
data = response.json()
print('total jokes', len(data['result']))
for joke in data['result']:
    print(joke['value'])