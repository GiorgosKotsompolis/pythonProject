import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors"
url_txt = requests.get(url).text
#print(url_txt)

s = BeautifulSoup(url_txt, "html.parser")
#print(s.prettify())

print(s.title)
print(s.title.string)