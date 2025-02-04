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


# params = {
#     "query": "eat"
# }
# response = requests.get("https://api.chucknorris.io/jokes/search", params)
# print(response.status_code)
# pprint.pprint(response.json())
# data = response.json()
# print('total jokes', len(data['result']))
# for joke in data['result']:
#     print(joke['value'])


# response = requests.get("https://api.chucknorris.io/jokes/categories")
# categories = response.json()
# print(categories)
# c = categories[0]
# # https://api.chucknorris.io/jokes/random?category={category}
# response = requests.get(
#     "https://api.chucknorris.io/jokes/random",
#     {"category": c}
# )
# print(response.url)
#
# "https://finnhub.io/api/v1/search?q=apple&exchange=US&token=cp310g9r01qvi2qqa9ogcp310g9r01qvi2qqa9p0"

api_key = "cp310g9r01qvi2qqa9ogcp310g9r01qvi2qqa9p0"

ticker = input("Insert ticker")
url = "https://finnhub.io/api/v1/search"
params = {
    "q": ticker,
    "exchange": "US",
    "token": api_key
}
response = requests.get(url, params)
pprint.pprint(response.json())