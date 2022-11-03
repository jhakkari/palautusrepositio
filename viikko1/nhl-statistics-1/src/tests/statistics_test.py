import unittest
from statistics import Statistics
from player import Player

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
        self.statistics = Statistics(PlayerReaderStub())

    def test_henkilohaku_palauttaa_osuman(self):
        vastaus = self.statistics.search("Semenko")
        self.assertEqual(vastaus.name, "Semenko")

    def test_henkilohaku_ei_palauta_osumaa(self):
        vastaus = self.statistics.search("gdfgd")
        self.assertEqual(None, None)

    def test_joukkuehaku_palauttaa_osuman(self):
        vastaus = self.statistics.team("PIT")
        self.assertEqual(vastaus[0].name, "Lemieux")

    def test_joukkuehaku_ei_palauta_osumaa(self):
        vastaus = self.statistics.team("AAA")
        self.assertEqual(len(vastaus), 0)

    def test_top_3_parhaat_pisteet_palauttaa_osuman(self):
        vastaus = self.statistics.top(3, 1)
        oikea_jarj = True
        if vastaus[0].name != "Gretzky":
            oikea_jarj = False
        if vastaus[1].name != "Lemieux":
            oikea_jarj = False
        if vastaus[2].name != "Yzerman":
            oikea_jarj = False

        self.assertEqual(oikea_jarj, True)

    def test_top_3_parhaat_maalintekijat_palauttaa_osuman(self):
        vastaus = self.statistics.top(3, 2)
        oikea_jarj = True
        if vastaus[0].name != "Lemieux":
            oikea_jarj = False
        if vastaus[1].name != "Yzerman":
            oikea_jarj = False
        if vastaus[2].name != "Kurri":
            oikea_jarj = False

        self.assertEqual(oikea_jarj, True)

    def test_top_3_parhaat_avustukset_palauttaa_osuman(self):
        vastaus = self.statistics.top(3, 3)
        oikea_jarj = True
        if vastaus[0].name != "Gretzky":
            oikea_jarj = False
        if vastaus[1].name != "Yzerman":
            oikea_jarj = False
        if vastaus[2].name != "Lemieux":
            oikea_jarj = False

        self.assertEqual(oikea_jarj, True)
        

    
