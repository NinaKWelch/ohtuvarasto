import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        #saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisays_ei_enemman_kuin_tilaa(self):
        self.varasto.lisaa_varastoon(11)

        lisatty_maara = self.varasto.saldo
        self.assertAlmostEqual(lisatty_maara, 10)

    def test_lisays_ei_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ottaminen_ei_enemman_kuin_varastossa(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(saatu_maara, 5)

    def test_ottaminen_ei_negatiivista_maaraa(self):
        saatu_maara = self.varasto.ota_varastosta(-2)

        self.assertEqual(saatu_maara, 0.0)

    def test_teksti_antaa_oikean_vastauksen(self):
        teksti = str(self.varasto)

        self.assertEqual(teksti, "saldo = 0, vielä tilaa 10")

    def test_varasto_ei_negatiivista_alkusaldoa(self):
        self.varasto = Varasto(10, alku_saldo = -2)
        
        self.assertEqual(self.varasto.saldo, 0.0)

    def test_varasto_ei_negatiivista_tilavuutta(self):
        self.varasto = Varasto(-2)

        self.assertEqual(self.varasto.tilavuus, 0.0)

