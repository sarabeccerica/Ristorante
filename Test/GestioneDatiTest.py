import unittest

from Sistema.GestioneDati import GestioneDati


class MyTestCase(unittest.TestCase):
    def test_GestioneDati(self):
        prova = dict()
        prova[1] = 'loris'
        prova[2] = 'sara'
        gestione = GestioneDati()
        self.assertEqual(gestione.numeroScontrini(prova), 2)


if __name__ == '__main__':
    unittest.main()
