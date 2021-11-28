import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuote1 = Tuote("nimi", 2)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_korin_hinta_sama_kuin_yhden_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.assertEqual(self.kori.hinta(), 2)
