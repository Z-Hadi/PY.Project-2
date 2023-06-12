import requests
import re
from bs4 import BeautifulSoup
url = "http://books.toscrape.com/catalogue/the-last-mile-amos-decker-2_754/index.html"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

universal_product_code= soup.find("th", string="UPC" ).next_sibling.get_text()
book_title= soup.find('li', class_="active").get_text()
price_including_tax= soup.find("th", string="Price (excl. tax)" ).next_sibling.get_text()
price_excluding_tax= soup.find("th", string="Price (incl. tax)" ).next_sibling.get_text()
quantity_available= soup.find(string=re.compile("In stock"))[24:27]
image_url =soup.find('img', attrs={"alt": book_title})['src']



test= soup.find("div", attrs={"id": "product_description"}).next_sibling

# #
# #Get string of HTML title
# print(soup.title.string)
# #Find all elements with <a> tag
# print(soup.find_all('a'))
# # Find element with id of “link1”
# print(soup.find(id="link1"))
# #Find all p elements with class “title”
# print(soup.find_all("p", class_="title"))
#
# titles = soup.find_all("a" , class_="gem-c-document-list__item-title")
#
# for title in titles:
#  print(title.string)

# bs_titles = soup.find_all("a", class_="gem-c-document-list__item-title")
# titles = []
# for title in bs_titles:
#     titles.append(title.string)


