from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

ycWebPage = response.text

soup = BeautifulSoup(ycWebPage, "html.parser")
# print(soup.title)

articles = soup.find_all(name = "span" ,class_ = "titleline")
# print(articleTag)
articleTexts = []
articleLinks = []

for article in articles:
    text = article.a.getText()
    articleTexts.append(text)
    link  = article.a.get("href")
    articleLinks.append(link)
articleUpvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name = "span", class_ = "score")]
# print(articleTexts)
# print(articleLinks)
# print(articleUpvotes)

highestScore = max(articleUpvotes)
indexOfHighestScore = articleUpvotes.index(highestScore)

print(articleTexts[indexOfHighestScore])
print(articleLinks[indexOfHighestScore])
print(f"Score : {highestScore}")












# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.string)

# # print(soup.li)

# allAnchorTags = soup.find_all(name="a")
# for tag in allAnchorTags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# sectionHeading = soup.find(name="h3", class_="heading")
# print(sectionHeading.getText())

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)