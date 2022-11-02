import unittest
from statistics import Statistics
from player import Player
from sortby import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_etsi_pelaajaa_joka_on_listassa(self):
        self.assertEqual(self.statistics.search("Semenko").name, "Semenko")
    
    def test_etsi_pelaajaa_joka_ei_ole_listassa(self):
        self.assertEqual(self.statistics.search("Jetro"), None)
    
    def test_etsi_kaikki_joukkueessa_pelaavat(self):
        self.assertEqual(self.statistics.team("EDM")[0].name, "Semenko")
    
    def test_etsi_eniten_pisteita_tehnyt_pelaaja(self):
        self.assertEqual(self.statistics.top(1, SortBy.POINTS)[0].name, "Gretzky")
    
    def test_haetaan_pelaajat_maalien_mukaan(self):
        self.assertEqual(self.statistics.top(1, SortBy.GOALS)[0].name, "Lemieux")
    
    def test_haetaan_eniten_syottoja_tehnyt_pelaaja(self):
        self.assertEqual(self.statistics.top(1, SortBy.ASSISTS)[0].name, "Gretzky")
    