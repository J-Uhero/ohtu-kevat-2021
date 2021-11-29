#KAPASITEETTI = 5
#OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self):
        self.lukujono = []

    def kuuluu(self, n):
        return n in self.lukujono

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lukujono.append(n)
            return True
        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.lukujono.remove(n)
            return True
        return False

    def mahtavuus(self):
        return len(self.lukujono)

    def to_int_list(self):
        return list(self.lukujono)

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        yhdiste = joukko_b.to_int_list()
        for a in joukko_a:
            if not joukko_b.kuuluu(a):
                yhdiste.lisaa(a)
        return yhdiste

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        leikkaus = IntJoukko()
        for a in joukko_a:
            if joukko_b.kuuluu(a):
                leikkaus.lisaa(a)
        return leikkaus

    @staticmethod
    def erotus(joukko_a, joukko_b):
        erotus = IntJoukko()
        for a in joukko_a:
            if not joukko_b.kuuluu(a):
                erotus.lisaa(a)
        return erotus

    def __str__(self):
        return str(self.lukujono)
