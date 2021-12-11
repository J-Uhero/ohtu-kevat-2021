class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self._tulos = tulos
        self._edellinen_tulos = 0

    @property
    def tulos(self):
        return self._tulos
    
    @tulos.setter
    def tulos(self, arvo):
        self._edellinen_tulos = self._tulos
        self._tulos = arvo
    
    def kumoa(self):
        self._tulos = self._edellinen_tulos

class Erotus:
    def __init__(self, sovellus):
        self._sovellus = sovellus
    
    def suorita(self, arvo):
        self._sovellus.tulos -= arvo

class Summa:
    def __init__(self, sovellus):
        self._sovellus = sovellus
    
    def suorita(self, arvo):
        self._sovellus.tulos += arvo

class Nollaus:
    def __init__(self, sovellus):
        self._sovellus = sovellus

    def suorita(self, arvo=0):
        self._sovellus.tulos = 0

class Kumoa:
    def __init__(self, sovellus):
        self._sovellus = sovellus

    def suorita(self, arvo):
        self._sovellus.kumoa()

    '''
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
        '''