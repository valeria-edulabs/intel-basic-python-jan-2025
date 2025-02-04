import requests

# https://api.chucknorris.io/jokes/random
# https://api.chucknorris.io/jokes/categories
# https://api.chucknorris.io/jokes/random?category={category}
# https://api.chucknorris.io/jokes/search?query={query}

response = requests.get("https://api.chucknorris.io/jokes/random")
print(response.status_code)
if response.status_code == 200:
    data = response.text
    print(type(data))
    data = response.json()
    print(data['value'])
# response = requests.get("https://api.chucknorris.io/jokes/randommmm")
# print(response.status_code)
