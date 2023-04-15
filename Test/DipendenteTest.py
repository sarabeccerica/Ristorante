import datetime
import unittest

from Servizio.Dipendente import Dipendente


class MyTestCase(unittest.TestCase):
    def test_Dipendente(self):
        prodotto = {
            "nome": 'sara',
            "cognome": 'becc',
            "dataNascita": datetime.datetime(year=2001,month=1,day=29),
            "codiceFiscale": 'bccsr',
            "email": 'sara@',
            "telefono": '389'
        }
        dip = Dipendente()
        dip.aggiungiDipendente('sara','becc',datetime.datetime(year=2001,month=1,day=29),'bccsr','sara@','pwd','389')
        self.assertEqual(dip.getDatiDipendente(), prodotto)


if __name__ == '__main__':
    unittest.main()
