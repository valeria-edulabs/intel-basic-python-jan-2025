import requests

proxies = {
    'http': 'http://proxy-chain.intel.com:911',
    'https': 'http://proxy-chain.intel.com:911',
}

url = "https://api.chucknorris.io/jokes/random"
requests.get(url, proxies=proxies)

