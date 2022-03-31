class C1:
    def __init__(self):
        self.field=""


def valami(field):
    pass

valami(C1.field)

#mindegyik elemnek van egy __dict__ "dungle" adattagja
#visszaadja az összes adattagját egy elemnek
#stringként fel vannak sorolva az elemek + metódusok