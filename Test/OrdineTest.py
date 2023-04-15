import unittest

from Gestione.Ordine import Ordine


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ordine = Ordine()
        self.assertEqual(ordine.inserimentoListaPiatti(), False)


if __name__ == '__main__':
    unittest.main()
