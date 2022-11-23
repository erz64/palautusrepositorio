import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.piima = Tuote("Piima", 5)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.piima)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tavaroiden(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.piima)

        self.assertEqual(self.kori.hinta(), 8)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tavaroiden(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 6)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(len(self.kori.ostokset()), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_lisatyn_tuotteen_nimi(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.ostokset()[0].tuotteen_nimi(), "Maito")
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_lisatyn_tuotteen_lukumaara(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 1)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.piima)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_vain_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(len(self.kori.tuotteet), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_tuote_jolla_sama_nimi_kuin_tuotteilla_ja_lukumaara(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.ostokset()[0].tuotteen_nimi(), "Maito")

        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 2)
    
    def test_jos_korissa_on_kaksi_tuotetta_ja_toinen_poistetaan_korissa_on_enaa_yksi_tuote(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.kori.poista_tuote(self.maito)

        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 1)
    