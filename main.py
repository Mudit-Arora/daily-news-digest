import requests

api_key = "de6c5474f9a34526b968574c151d2bdb"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-06&sortBy=publishedAt&apiKey=de6c5474f9a34526b968574c151d2bdb"

# Make request
requests = requests.get(url)

# Get a dict with data
content = requests.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])