import requests
from bs4 import BeautifulSoup
from Character import Character


def get_arr(r):
    redChars = list()

    redSoup = BeautifulSoup(r.text, "lxml")

    namesoup = redSoup.find_all('div', class_='mw-category-group')

    for i in namesoup:
        catNames = i.find_all('a', href=True)
        for j in catNames:
            redChars.append(Character(j['title'].split(' ')[0], "http://www.serenesforest.net" + j['href']))
    return redChars


def main():
    redURL = 'https://serenesforest.net/wiki/index.php/Category:RedCard'
    redlink = requests.get(redURL)
    redArr = get_arr(redlink)

    blueURL = 'https://serenesforest.net/wiki/index.php/Category:BlueCard'
    bluelink = requests.get(blueURL)
    blueArr = get_arr(bluelink)

    whiteURL = 'https://serenesforest.net/wiki/index.php/Category:WhiteCard'
    whitelink = requests.get(whiteURL)
    whiteArr = get_arr(whitelink)

    blackURL = 'https://serenesforest.net/wiki/index.php/Category:BlackCard'
    blacklink = requests.get(blueURL)
    blackArr = get_arr(blacklink)

    greenURL = 'https://serenesforest.net/wiki/index.php/Category:GreenCard'
    greenlink = requests.get(greenURL)
    greenArr = get_arr(greenlink)

    purpleURL = 'https://serenesforest.net/wiki/index.php/Category:PurpleCard'
    purplelink = requests.get(purpleURL)
    purpleArr = get_arr(purplelink)

    yellowURL = 'https://serenesforest.net/wiki/index.php/Category:YellowCard'
    yellowlink = requests.get(yellowURL)
    yellowArr = get_arr(yellowlink)

    colorlessURL = 'https://serenesforest.net/wiki/index.php/Category:ColorlessCard'
    colorlesslink = requests.get(colorlessURL)
    colorlessArr = get_arr(colorlesslink)

    colorlessArr[0].fill_cards()


if __name__ == "__main__":
    main()
