import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")

for book in books:
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    cost = book.select(".price_color")[0].get_text()
    print(f"Book title: {title} ||| Rating: {rating} stars ||| Cost: {cost}")

input("Enter any key for exit..............")