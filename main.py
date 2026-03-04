import requests

query = input("What are the type of news you're interested todey?:")
api = "82a46ea6c4d948458f5d982c3adf1097"
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-01-10&sortBy=publishedAt&apiKey={api}"

print(url)
c = requests.get(url)
data = c.json()
articales = data["articles"]

for index, article in enumerate(articales):
  print(index + 1, article["title"])
  print(article["url"])
  print("\n*******************\n")