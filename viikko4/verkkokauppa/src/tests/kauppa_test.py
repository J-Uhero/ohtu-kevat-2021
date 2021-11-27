import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_a_mock = Mock()
        self.viitegeneraattori_a_mock = Mock(wraps=Viitegeneraattori())
        self.varasto_a_mock = Mock(wraps=Varasto())
        self.kauppa_a = Kauppa(self.varasto_a_mock, self.pankki_a_mock, self.viitegeneraattori_a_mock)


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_yhden_tuotteen_ostossa_tilisiirto_suoritetaan_oikein(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 42
        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 2:
                return 100
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 2:
                return Tuote(2, "kalja", 3)
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Minttu", "23456")

        pankki_mock.tilisiirto.assert_called_with("Minttu", 42, "23456", "33333-44455", 3)

    def test_kahden_eri_tuotteen_ostossa_tilisiirto_suoritetaan_oikein(self):

        self.kauppa_a.aloita_asiointi()
        self.kauppa_a.lisaa_koriin(1)
        self.kauppa_a.lisaa_koriin(5)
        self.kauppa_a.tilimaksu("Ville", "34567")
        self.pankki_a_mock.tilisiirto.assert_called_with("Ville", 2, "34567", "33333-44455", 7)
    
    def test_kahden_saman_tuotteen_ostossa_tilisiirto_suoritetaan_oikein(self):

        self.kauppa_a.aloita_asiointi()
        self.kauppa_a.lisaa_koriin(1)
        self.kauppa_a.lisaa_koriin(1)
        self.kauppa_a.tilimaksu("Jari", "45678")
        self.pankki_a_mock.tilisiirto.assert_called_with("Jari", 2, "45678", "33333-44455", 6)

    def test_lisatty_tuote_loppu_tilisiirto_oikein(self):

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 100
            if tuote_id == 2:
                return 0 
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "ES", 2)
            if tuote_id == 2:
                return Tuote(2, "kalja", 3)
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, self.pankki_a_mock, self.viitegeneraattori_a_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Mari", "56789")
        self.pankki_a_mock.tilisiirto.assert_called_with("Mari", 2, "56789", "33333-44455", 2)

    def test_aloita_asiointi_nollaa_edelliset_tiedot(self):
        self.kauppa_a.aloita_asiointi()
        self.kauppa_a.lisaa_koriin(1)
        self.kauppa_a.lisaa_koriin(2)
        self.kauppa_a.tilimaksu("Romeo", "12345")
        self.pankki_a_mock.tilisiirto.assert_called_with("Romeo", 2, "12345", "33333-44455", 4)

        self.kauppa_a.aloita_asiointi()
        self.kauppa_a.lisaa_koriin(1)
        self.kauppa_a.lisaa_koriin(5)
        self.kauppa_a.tilimaksu("Julia", "54321")
        self.pankki_a_mock.tilisiirto.assert_called_with("Julia", 3, "54321", "33333-44455", 7)
    
    def test_joka_maksulla_pyydetaan_uusi_viite(self):
        self.kauppa_a.aloita_asiointi()
        self.kauppa_a.lisaa_koriin(1)
        self.kauppa_a.tilimaksu("Romeo", "12345")
        self.assertEqual(self.viitegeneraattori_a_mock.uusi.call_count, 1)

        self.kauppa_a.aloita_asiointi()
        self.kauppa_a.lisaa_koriin(1)
        self.kauppa_a.tilimaksu("Julia", "54321")
        self.assertEqual(self.viitegeneraattori_a_mock.uusi.call_count, 2)

    def test_korista_poisto_onnistuu(self):
        
        self.kauppa_a.aloita_asiointi()
        self.kauppa_a.lisaa_koriin(1)
        self.kauppa_a.lisaa_koriin(2)
        self.kauppa_a.poista_korista(1)
        self.kauppa_a.tilimaksu("Nti Groove", "13579")
        self.pankki_a_mock.tilisiirto.assert_called_with("Nti Groove", 2, "13579", "33333-44455", 1)
