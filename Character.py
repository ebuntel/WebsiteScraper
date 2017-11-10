class Character:
    name = ""

    #Character Info#
    color = ""
    charclass = ""
    range = ""
    insig = ""
    gender = ""
    weapon = ""
    other = ""
    cost = 0
    promotion = 0
    attack = 0
    support = 0
    series = ""
    illustrator = ""
    quote = ""
    skillichi = ""
    skillni = ""
    skillsan = ""
    skillyon = ""
    skillgo = ""
    supportskill = ""
    #\Character Info#

    def __init__(self, title):
        self.name = title

    def addInfo(self, col):
        self.color = col


