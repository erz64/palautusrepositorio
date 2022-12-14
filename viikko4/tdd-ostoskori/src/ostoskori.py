from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tuotteet = []
        self.lkm = 0
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        for tuote in self.tuotteet:
            self.lkm += tuote.lukumaara()
        return self.lkm
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for tuote in self.tuotteet:
            summa += tuote.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = Ostos(lisattava)
        for tuote in self.tuotteet:
            if tuote.tuotteen_nimi() == ostos.tuotteen_nimi():
                tuote.muuta_lukumaaraa(1)
                return
        else:
            self.tuotteet.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        ostos = Ostos(poistettava)
        for tuote in self.tuotteet:
            if tuote.tuotteen_nimi() == ostos.tuotteen_nimi():
                if tuote.lukumaara() > 1:
                    tuote.muuta_lukumaaraa(-1)
                else:
                    self.tuotteet.remove(tuote)

    def tyhjenna(self):
        self.tuotteet = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.tuotteet
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
