import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.tyhja_maksukortti = Maksukortti(0)

    def test_alussa_1000_euroa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_lounaita_alussa_0(self):
        self.assertEqual(self.kassa.maukkaat + self.kassa.edulliset, 0)

    def test_lounaiden_maarat_kasvaa_oikein_kateisella(self):
        self.kassa.syo_maukkaasti_kateisella(500) #+1
        self.kassa.syo_maukkaasti_kateisella(100)
        self.kassa.syo_edullisesti_kateisella(300) #+1
        self.kassa.syo_edullisesti_kateisella(100)

        self.assertEqual((self.kassa.edulliset,  self.kassa.maukkaat), (1, 1))

    def test_riittava_kateismaksu_vaihtoraha_toimii(self):
        edullinen_vaihtoraha = self.kassa.syo_edullisesti_kateisella(500)
        maukas_vaihtoraha = self.kassa.syo_maukkaasti_kateisella(500)

        self.assertEqual((edullinen_vaihtoraha, maukas_vaihtoraha), (260, 100))

    def test_riittamaton_kateismaksu__vaihtoraha_toimii(self):
        edullinen_vaihtoraha = self.kassa.syo_edullisesti_kateisella(100)
        maukas_vaihtoraha = self.kassa.syo_maukkaasti_kateisella(100)

        self.assertEqual((edullinen_vaihtoraha, maukas_vaihtoraha), (100, 100))

    def test_riittava_kateismaksu_lisaantyy_kassaan(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.kassa.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000 + 240 + 400)

    def test_riittamaton_kateismaksu_ei_lisaannu_kassaan(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.kassa.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_korttimaksu_kasvattaa_lounaiden_maaria_oikein(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)#+1
        self.kassa.syo_edullisesti_kortilla(self.tyhja_maksukortti)
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)#+1
        self.kassa.syo_maukkaasti_kortilla(self.tyhja_maksukortti)

        self.assertEqual((self.kassa.edulliset, self.kassa.maukkaat), (1, 1))

    def test_veloitus_oikein_kun_rahaa_riittää(self):
        first = self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        second = self.kassa.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual((first, second, self.maksukortti.saldo), (True, True, 1000 - 240 - 400))

    def test_veloitus_oikein_kun_rahaa_riittamattomasti(self):
        first = self.kassa.syo_edullisesti_kortilla(self.tyhja_maksukortti)
        second = self.kassa.syo_maukkaasti_kortilla(self.tyhja_maksukortti)

        self.assertEqual((first, second, self.maksukortti.saldo), (False, False, 1000))

    def test_kassan_rahamaara_ei_muutu_kortilla_maksaessa(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassa.syo_edullisesti_kortilla(self.tyhja_maksukortti)
        self.kassa.syo_maukkaasti_kortilla(self.tyhja_maksukortti)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortille_ladatessa_kassan_raha_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, 1000)

        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_kortille_ladattaessa_kortin_saldo_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, 1000)

        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_kortille_ladattaessa_negatiivinen_summa_ei_tee_mitään(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)