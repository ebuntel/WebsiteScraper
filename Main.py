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

def get_characters(name_array):
    charlist = list()
    for i in name_array:
        charlist.append(i.fill_cards())
    return charlist

def main():
    redURL = 'https://serenesforest.net/wiki/index.php/Category:RedCard'
    redlink = requests.get(redURL)
    redArr = get_arr(redlink)
    red_char_arr = get_characters(redArr)

    blueURL = 'https://serenesforest.net/wiki/index.php/Category:BlueCard'
    bluelink = requests.get(blueURL)
    blueArr = get_arr(bluelink)
    blue_char_arr = get_characters(blueArr)

    whiteURL = 'https://serenesforest.net/wiki/index.php/Category:WhiteCard'
    whitelink = requests.get(whiteURL)
    whiteArr = get_arr(whitelink)
    white_char_arr = get_characters(whiteArr)

    blackURL = 'https://serenesforest.net/wiki/index.php/Category:BlackCard'
    blacklink = requests.get(blackURL)
    blackArr = get_arr(blacklink)
    black_char_arr = get_characters(blackArr)

    greenURL = 'https://serenesforest.net/wiki/index.php/Category:GreenCard'
    greenlink = requests.get(greenURL)
    greenArr = get_arr(greenlink)
    green_char_arr = get_characters(greenArr)

    purpleURL = 'https://serenesforest.net/wiki/index.php/Category:PurpleCard'
    purplelink = requests.get(purpleURL)
    purpleArr = get_arr(purplelink)
    purple_char_arr = get_characters(purpleArr)

    yellowURL = 'https://serenesforest.net/wiki/index.php/Category:YellowCard'
    yellowlink = requests.get(yellowURL)
    yellowArr = get_arr(yellowlink)
    yellow_char_arr = get_characters(yellowArr)

    colorlessURL = 'https://serenesforest.net/wiki/index.php/Category:ColorlessCard'
    colorlesslink = requests.get(colorlessURL)
    colorlessArr = get_arr(colorlesslink)
    colorless_char_arr = get_characters(colorlessArr)

    print(colorless_char_arr[0].print_cards())

if __name__ == "__main__":
    main()
