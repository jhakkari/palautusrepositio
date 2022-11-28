import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)

    def test_ostoskorin_tavaroiden_lkm_alussa(self):
        self.assertAlmostEqual(self.kori.tavaroita_korissa(), 0)
