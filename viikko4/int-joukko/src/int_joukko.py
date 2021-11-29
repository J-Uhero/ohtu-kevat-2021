#KAPASITEETTI = 5
#OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self):
        self.lukujono = []

        #self.kasvatuskoko = max(kasvatuskoko, OLETUSKASVATUS)
        
        '''
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko'''
        #self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.lukujono
        '''luku = 0
        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujono[i]:
                luku += 1
        return luku > 0'''


    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lukujono.append(n)
            return True
        return False
        '''if self.alkioiden_lkm == 0:
            self.lukujono[0] = n
            self.alkioiden_lkm += 1
            return True'''

        
        '''
        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.lukujono) == 0:
                taulukko_old = self.lukujono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)

            return True
        return False'''

    def poista(self, n):
        if self.kuuluu(n):
            self.lukujono.remove(n)
            return True
        return False
    
        
        '''
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.ljono[j]
                self.ljono[j] = self.ljono[j + 1]
                self.ljono[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False
    
    def kopioi_taulukko(self, taulukko):
        return list(taulukko)'''

    def mahtavuus(self):
        return len(self.lukujono)

    def to_int_list(self):
        return list(self.lukujono)
        '''
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu'''

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        yhdiste = joukko_b.to_int_list()
        for a in joukko_a:
            if not joukko_b.kuuluu(a):
                yhdiste.lisaa(a)
        return yhdiste
        '''
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x'''

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        leikkaus = IntJoukko()
        for a in joukko_a:
            if joukko_b.kuuluu(a):
                leikkaus.lisaa(a)
        return leikkaus
        '''
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y'''

    @staticmethod
    def erotus(joukko_a, joukko_b):
        erotus = IntJoukko()
        for a in joukko_a:
            if not joukko_b.kuuluu(a):
                erotus.lisaa(a)
        return erotus
        '''
        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z'''

    def __str__(self):
        return str(self.lukujono)
        '''
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos'''
