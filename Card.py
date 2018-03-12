class Card:
    name = ""

    # Character Info#
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
    comment = ""
    # \Character Info#

    def __init__(self, title):
        self.name = title

    def add_info(self, arr):
        self.color = arr[0]
        self.charclass = arr[1]
        self.range = arr[2]
        self.insig = arr[3]
        self.gender = arr[4]
        self.weapon = arr[5]
        self.other = arr[6]
        self.cost = arr[7]
        self.promotion = arr[8]
        self.attack = arr[9]
        self.support = arr[10]
        self.series = arr[11]
        self.illustrator = arr[12]
        self.quote = arr[13]
        self.skillichi = arr[14]
        self.skillni = arr[15]
        self.skillsan = arr[16]
        self.skillyon = arr[17]
        self.skillgo = arr[18]
        self.supportskill = arr[19]
        self.comment = arr[20]





