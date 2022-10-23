
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

empireWebPage = response.text

soup = BeautifulSoup(empireWebPage, 'html.parser')

movieTitles = [title.text for title in soup.find_all(name = "h3", class_ = "title")]
titles = movieTitles[::-1] #reverse the index of movie titles list
file = open("top-100-movies.txt", "w")
for movie_title in titles:
    file.write(movie_title + "\n")
file.close()

file = open("top-100-movies.txt", "r")
print(file.read())


