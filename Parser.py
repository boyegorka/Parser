from bs4 import BeautifulSoup
import requests

circle = 0
href = ""

while True:
    if circle == 0:
        url = "https://www.kinopoisk.ru/lists/top250/"
    else:
        url = "https://www.kinopoisk.ru" + href
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    print(f"-------------------- {circle + 1} Page --------------------")
    for block in soup.find_all("div", class_="desktop-rating-selection-film-item"):
        index = block.find("span" , {"class" : "film-item-rating-position__position"}).text
        name = block.find("p", {"class" : "selection-film-item-meta__name"}).text
        fullName = block.find("p", {"class" : "selection-film-item-meta__original-name"}).text
        country = block.find("span", {"class" : "selection-film-item-meta__meta-additional-item"}).text
        rating = block.find("span", {"class":"rating__value rating__value_positive"}).text
        print(f"{index} {name} {fullName} {country} {rating}")

    if circle >= 1 and circle <= 4:
        nextButton = soup.find_all("a", {"class" : "paginator__page-relative"})[1]
    else:
        nextButton = soup.find("a", {"class" : "paginator__page-relative"})

    if nextButton == None:
        break
    href = nextButton.get("href")
    circle +=1