class Eksponat:
    def __init__(self, nom, yil):
        self.nom = nom
        self.yil = yil

class Muzey:
    def __init__(self):
        self.eksponatlar = []

    def eksponat_qosh(self, eksponat):
        self.eksponatlar.append(eksponat)

    def yil_eksponatlari(self, yil):
        return [e for e in self.eksponatlar if e.yil == yil]



m = Muzey()
m.eksponat_qosh(Eksponat("Vaza", 1890))
m.eksponat_qosh(Eksponat("Haykal", 1890))
m.eksponat_qosh(Eksponat("Rasm", 1900))

for e in m.yil_eksponatlari(1890):
    print(e.nom)
