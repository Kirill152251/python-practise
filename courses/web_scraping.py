import requests
import bs4

url = "http://quotes.toscrape.com/page/{}/"
page = 1
authors_set = set()
while True:
    data = requests.get(url.format(page))
    soup = bs4.BeautifulSoup(data.text, "lxml")
    authors = soup.select(".author")
    if len(authors) == 0:
        break
    else:
        for item in authors:
            authors_set.add(item.text)
    page += 1

[print(x) for x in sorted(authors_set)]
