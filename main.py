import requests
import re
import csv
from bs4 import BeautifulSoup, Comment

headers = ["product_page_url", "universal_product_code", "book_title", "price_incl_tax", "price_excl_tax" , "qnt_available", "product_description", "category",  "review_rating", "image_url"]
url = "https://books.toscrape.com/catalogue/the-last-mile-amos-decker-2_754"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
product_page_url =(soup.find('p', class_="instock availability").find_next_sibling("p").contents[11].replace('<small><a href="','').replace('/reviews/">','').replace('0 customer reviews','').replace('</a></small>','').replace('\n','').replace(' /catalogue/','https://books.toscrape.com/catalogue/'))
universal_product_code= soup.find("th", string="UPC" ).next_sibling.get_text()
book_title= soup.find('li', class_="active").get_text()
price_incl_tax= soup.find("th", string="Price (excl. tax)" ).next_sibling.get_text()
price_excl_tax= soup.find("th", string="Price (incl. tax)" ).next_sibling.get_text()
qnt_available= soup.find(string=re.compile("In stock"))[24:26]
product_description = soup.find("div", attrs={"id": "product_description", "class": "sub-header"}).find_next_sibling("p").get_text()
category = soup.find("ul", class_="breadcrumb").find_all("a", limit=3)[-1].get_text()
review_rating= str(soup.find('p', class_="instock availability").find_next_sibling("p")["class"][-1])+" stars"
image_url =(soup.find('img', attrs={"alt": book_title})['src'].replace('../../media/','https://books.toscrape.com/catalogue/media/'))

headers_values = ["product_page_url", "universal_product_code", "book_title", "price_incl_tax", "price_excl_tax" , "qnt_available", "product_description", "category",  "review_rating", "image_url"]

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    for i in range(len(headers)):
        writer.writerow(str(headers_values[i]))





