from bs4 import BeautifulSoup
import json
import pprint
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "fd16f7064cec4afbada18ff2c652364c"
SPOTIPY_CLIENT_SECRET = "bca6b6a20b724a4781c311ed09400d75"
REDIRECT_URI = "http://example.com"

scope = "playlist-modify-private"
auth_manager = SpotifyOAuth(scope=scope, client_secret=SPOTIPY_CLIENT_SECRET,
                            client_id=SPOTIPY_CLIENT_ID, redirect_uri=REDIRECT_URI,
                            show_dialog=True,
                            cache_path="token.txt")
sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()["id"]

# TODO 1: Create list of Spotify song URIs for the list of song names found from step 1
# TODO 1?: lookup how to make a playlist using spotipy


response = requests.get(f"https://www.billboard.com/charts/hot-100/1996-12-18/")
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
all_track_titles = [tag.getText().strip() for tag in soup.select(selector=".c-title.a-no-trucate")]  # > finds tags DIRECTLY beneath other tags, no deeper children

# TODO 1a: Find track URI
track_uri = sp.search(q=f"{all_track_titles[0]},1996", type="track", limit=1)["tracks"]["items"][0]["uri"]
print(track_uri)

# TODO 1b: get a list of 100 track URIs
all_track_uris = [sp.search(q=f"{track_title},1996", type="track", limit=1)["tracks"]["items"][0]["uri"]
                  for track_title in all_track_titles]

# TODO: 1c: handle IndexError for when there is no track available
print(all_track_uris)
# for song_title in all_song_titles:
#     print(f"{all_song_titles.index(song_title)+1}) " + song_title)

TEST_URI = "spotify:track:5Ihd9HrPvOADyVoonH9ZjB"


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

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# -----------------------------------------------------------------------------------------------#

# -----------------------------------------------------------------------------------------------#
# all_song_titles.reverse()  # no need to assign this to a variable, interestingly
# all_titles[::-1]  # could work as well

# with open("movies.txt", mode="w", encoding="utf-8") as file:
#     for title in all_song_titles:
#         file.write(f"{title}\n")

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
