KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.tarkista_arvo(kapasiteetti)
        self.kasvatuskoko = self.tarkista_arvo(kasvatuskoko)
        self.lista = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0
    
    def tarkista_arvo(self, arvo):
        if arvo is None:
            arvo = KAPASITEETTI
        elif not isinstance(arvo, int) or arvo < 0:
            raise Exception("Väärä kapasiteetti") 
        return arvo

    def kuuluu(self, n):
        for alkio in self.lista:
            if alkio == n:
                return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lista[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            if self.onko_taynna():
                vanha_taulukko = self.lista
                self.kopioi_taulukko(self.lista, vanha_taulukko)
                self.lista = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(vanha_taulukko, self.lista)
            return True
        return False
    
    def onko_taynna(self):
        if self.alkioiden_lkm == len(self.lista):
            return True

    def poista(self, n):
        if n in self.lista:
            self.lista.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lista[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lista[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lista[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lista[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
