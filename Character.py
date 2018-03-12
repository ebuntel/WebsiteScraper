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

    def fill_cards(self):
        URL = self.link
        gotlink = requests.get(URL)
        soup = BeautifulSoup(gotlink.text, 'lxml')
        tables = soup.find_all('table', class_='sf')

        for i in tables:
            text = i.find('th').get_text()  # name of card
            trxt = i.find_all('td')

            listfortext = list()

            crd = Card(text)

            for j in trxt:
                txtarr = j.get_text()
                listfortext.append(txtarr)
                # print(txtarr[txtarr.index("\nClass")+1])
                # print(j.get_text())

            # Retrieve information about the card and store it in a temp variable #
            clss = listfortext[listfortext.index("Class\n") + 1]  # Class
            rng = listfortext[listfortext.index("Range\n") + 1]  # Range
            insignia = listfortext[listfortext.index("Insignia\n") + 1]  # Insignia
            gender = listfortext[listfortext.index("Gender\n") + 1]  # Gender
            weapon = listfortext[listfortext.index("Weapon\n") + 1]  # Weapon
            other = listfortext[listfortext.index("Other\n") + 1]  # Other
            cost = listfortext[listfortext.index("Cost\n") + 1]  # Cost
            promotion = listfortext[listfortext.index("Promotion\n") + 1]  # Promotion
            attack = listfortext[listfortext.index("Attack\n") + 1]  # Attack
            support = listfortext[listfortext.index("Support\n") + 1]  # Support
            series = listfortext[listfortext.index("Series\n") + 1]  # Series
            illustrator = listfortext[listfortext.index("Illustrator\n") + 1]  # Illustrator
            quote = listfortext[listfortext.index("Quote\n") + 1]  # Quote
            support_skill = listfortext[listfortext.index("Support Skill\n") + 1]  # Support Skill
            comments = listfortext[listfortext.index("Comments\n") + 1]  # Comments

            # NEED ERROR HANDLING AS NOT ALL UNITS HAVE ALL SKILLS
            skill_ichi = listfortext[listfortext.index("Skill 1\n") + 1]  # Skill one
            skill_ni = listfortext[listfortext.index("Skill 2\n") + 1]  # Skill two


