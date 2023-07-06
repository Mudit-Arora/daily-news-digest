import requests

api_key = "de6c5474f9a34526b968574c151d2bdb"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-06&sortBy=publishedAt&apiKey=de6c5474f9a34526b968574c151d2bdb"

requests = requests.get(url)
content = requests.text
print(content)