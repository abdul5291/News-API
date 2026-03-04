import requests

query = input("What are the type of news you're interested todey?:")
api = API_KEY # Enter your API Here
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-01-10&sortBy=publishedAt&apiKey={api}"

print(url)
c = requests.get(url)
data = c.json()
articales = data["articles"]

for index, article in enumerate(articales):
  print(index + 1, article["title"])
  print(article["url"])

  print("\n*******************\n")
