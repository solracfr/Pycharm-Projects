from bs4 import BeautifulSoup
import requests

# import lxml  # used if html parsing doesn't work
#
# # needs utf-8 encoding to access this file, likely cause of
# # the heart emoji
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")  # pass in contents of website and the kind of parser to use
# print(soup.title)  # gets full html line
# print(soup.title.name)  # gets just the html tag title
# print(soup.title.string)  # gets the string inside the html tag
#
# print(soup.a)  # prints the first <a> tag seen. works the same way with all other tags
#
# print(soup)  # prints the whole html file in one line
# print(soup.prettify())  # prints the whole html file with correct indentation
#
# all_anchor_tags = soup.find_all(name="a")  # prints all lines with the chosen tag as a string arg
#
# for tag in all_anchor_tags:
#     print(tag.getText())  # get just the text from the html line
#     print(tag.get("href"))  # get an attribute from the html line as a string arg
#
# print(all_anchor_tags)
#
# heading = soup.find(name="h1", id="name")  # can use id attribute as an arg
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")  # can also do class but it should be written as "class_"
# print(section_heading.get("class"))  # grab the class of the html line
#
# # select one anchor tag nested within a paragraph tag
# # naming convention is the same as selecting tags for CSS
# # Examples: "p a", ".class", "#id"
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")
all_titles = [tag.getText() for tag in soup.find_all(name="h3", class_="title")]  # > finds tags DIRECTLY beneath other tags, no deeper children
all_titles.reverse()  # no need to assign this to a variable, interestingly
# all_titles[::-1]  # could work as well

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for title in all_titles:
        file.write(f"{title}\n")

# #  two ways of finding something... I'm more partial to select right now
# article_upvote = soup.select_one(selector=".score")
# print(article_upvote.getText())
# article_upvote_2 = soup.find(name="span", class_="score")
# print(article_upvote_2.getText())
#
# #  two more ways of finding something... still more partial to select
# article_link = soup.select_one(selector=".titleline > a")
# print(article_link["href"])  # select attribute like you would with a list or dict
# print(article_link.get("href"))  # this works too
# # using find() requires searching again on that same object
# article_link_2 = soup.find(name="span", class_="titleline")
# print(article_link_2)
# article_link_2 = article_link_2.find(name="a")  # results are themselves searchable
# print(article_link_2)
