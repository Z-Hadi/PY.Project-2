import requests
from bs4 import BeautifulSoup
url = "http://books.toscrape.com/catalogue/the-project_856/index.html"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)
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
