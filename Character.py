import requests
from bs4 import BeautifulSoup
from Card import Card


class Character:
    name = ""
    cards = list()
    link = ""

    def __init__(self, title, link):
        self.name = title
        self.link = link

    def __str__(self):
        return "<" + self.name + " , " + self.link + ">"

    def print_cards(self):
        for i in self.cards:
            print(i)

    def fill_cards(self):
        URL = self.link
        gotlink = requests.get(URL)
        soup = BeautifulSoup(gotlink.text, 'lxml')
        tables = soup.find_all('table', class_='sf')

        for i in tables:
            text = i.find('th').get_text()  # name of card
            trxt = i.find_all('td')  # Rest of the text of the card

            listfortext = list()

            crd = Card(text)

            for j in trxt:
                txtarr = j.get_text()
                listfortext.append(txtarr)

            # Retrieve information about the card and store it in a temp variable #
            clss = listfortext[listfortext.index("Class\n") + 1]  # Class
            rng = listfortext[listfortext.index("Range\n") + 1]  # Range
            insignia = listfortext[listfortext.index("Insignia\n") + 1]  # Insignia
            gender = listfortext[listfortext.index("Gender ") + 1]  # Gender
            weapon = listfortext[listfortext.index("Weapon ") + 1]  # Weapon
            other = listfortext[listfortext.index("Other") + 1]  # Other
            cost = listfortext[listfortext.index("Cost") + 1]  # Cost
            promotion = listfortext[listfortext.index("Promotion\n") + 1]  # Promotion
            attack = listfortext[listfortext.index("Attack\n") + 1]  # Attack
            support = listfortext[listfortext.index("Support\n") + 1]  # Support
            series = listfortext[listfortext.index("Series\n") + 1]  # Series
            illustrator = listfortext[listfortext.index("Illustrator\n") + 1]  # Illustrator
            quote = listfortext[listfortext.index("Quote\n") + 1]  # Quote

            # NEED ERROR HANDLING AS NOT ALL UNITS HAVE ALL SKILLS
            try:
                support_skill = listfortext[listfortext.index("Support Skill") + 1]  # Support Skill
            except ValueError:
                print("HAPPENED S")
                support_skill = ""
            try:
                skill_ichi = listfortext[listfortext.index("Skill 1\n") + 1]  # Skill one
            except ValueError:
                print("HAPPENED 1")
                skill_ichi = ""
            try:
                skill_ni = listfortext[listfortext.index("Skill 2\n") + 1]  # Skill two
            except ValueError:
                print("HAPPENED 2")
                skill_ni = ""
            try:
                skill_san = listfortext[listfortext.index("Skill 3\n") + 1]  # Skill three
            except ValueError:
                print("HAPPENED 3")
                skill_san = ""
            try:
                skill_yon = listfortext[listfortext.index("Skill 4\n") + 1]  # Skill four
            except ValueError:
                print("HAPPENED 4")
                skill_yon = ""
            try:
                skill_go = listfortext[listfortext.index("Skill 5\n") + 1]  # Skill five
            except ValueError:
                print("HAPPENED 5")
                skill_go = ""

            # Add the info of the card to the previously created card object
            crd.add_info([find_color(insignia), clss, rng, insignia, gender, weapon, other, cost, promotion,
                          attack, support, series, illustrator, quote, skill_ichi, skill_ni, skill_san, skill_yon,
                          skill_go, support_skill
                          ])
            self.cards.append(crd)  # Add card to the list
        return self


def find_color(x):
    return {
        "Blade of Light": "Red",
        "Mark of Naga": "Blue",
        "Hoshido": "White",
        "Nohr": "Black",
        "Hoshido / Nohr": "Black and White",
        "Medallion": "Green",
        "Divine Weapons (Purple)": "Purple",
        "Holy War Flag": "Yellow",
    }.get(x, "Colorless")
