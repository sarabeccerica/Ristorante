import os
import pickle

class Ordine:

    def __init__(self):
        self.codice = 0
        self.statoOrdine = ""
        self.listaPiatti= dict()

    def aggiungiOrdine(self, numeroTavolo, listapiatti):
        ordini = dict()
        if self.controlloNumeroTavolo(numeroTavolo):
            self.codice = self.assegnamentoCodice(numeroTavolo)
            self.statoOrdine = "In Preparazione"
            self.inserimentoPiatti(listapiatti)
            if os.path.isfile('Dati\Ordini.pickle'):
                with open('Dati\Ordini.pickle', 'rb') as f:
                    ordini = dict(pickle.load(f))
            ordini[self.codice] = self
            with open('Dati\Ordini.pickle', 'wb') as f:
                pickle.dump(ordini, f, pickle.HIGHEST_PROTOCOL)

    def controlloNumeroTavolo(self,numeroTavolo):
        if os.path.isfile('Dati\Tavoli.pickle'):
            with open('Dati\Tavoli.pickle', 'rb') as f:
                tavoli = dict(pickle.load(f))
                for tavolo in tavoli.values():
                    if tavolo.numero == numeroTavolo and tavolo.stato == 'Occupato':
                        return True
                raise Exception("Numero tavolo non valido")

    def assegnamentoCodice(self, numeroTavolo):
        codice = (numeroTavolo*100)+1
        if os.path.isfile('Dati\Ordini.pickle'):
            with open('Dati\Ordini.pickle', 'rb') as f:
                ordini = dict(pickle.load(f))
                for i in ordini.keys():
                    if int(i/100) == numeroTavolo:
                        if i >= codice:
                            codice = i + 1
        return codice

    def calcoloTavoloOrdine(self):
        return int(self.codice/100)

    def inserimentoPiatti(self, listaPiatti):
        for piatto in listaPiatti.keys():
            if self.piattoNelMenu(piatto):
                self.listaPiatti[piatto] = listaPiatti[piatto]
            else:
                self.listaPiatti.clear()
                raise Exception("Piatto non presente nel menu")


    def piattoNelMenu(self, numeroPiatto):
        if os.path.isfile('Dati\Piatti.pickle'):
            with open('Dati\Piatti.pickle', 'rb') as f:
                piatti = dict(pickle.load(f))
                for piatto in piatti.values():
                    if piatto.numero == numeroPiatto:
                        return True
                return False
        else:
            return False

    def eliminaOrdine(self,codice):
        if os.path.isfile('Dati\Ordini.pickle'):
            with open('Dati\Ordini.pickle', 'rb') as f:
                ordini = dict(pickle.load(f))
                del ordini[codice]
            with open('Dati\Ordini.pickle', 'wb') as f:
                pickle.dump(ordini, f, pickle.HIGHEST_PROTOCOL)
        self.statoOrdine = ""
        self.listaPiatti = []
        self.codice = 0
        del self

    def ordinePreparato(self, codice):
        if os.path.isfile('Dati\Ordini.pickle'):
            with open('Dati\Ordini.pickle', 'rb') as f:
                ordini = dict(pickle.load(f))
                for ordine in ordini.values():
                    if ordine.codice == codice:
                        ordine.statoOrdine = "Preparato"
        with open('Dati\Ordini.pickle', 'wb') as f:
            pickle.dump(ordini, f, pickle.HIGHEST_PROTOCOL)

    def ordineConsegnato(self,codice):
        if os.path.isfile('Dati\Ordini.pickle'):
            with open('Dati\Ordini.pickle', 'rb') as f:
                ordini = dict(pickle.load(f))
                for ordine in ordini.values():
                    if ordine.codice == codice:
                        ordine.statoOrdine = "Consegnato"
        with open('Dati\Ordini.pickle', 'wb') as f:
            pickle.dump(ordini, f, pickle.HIGHEST_PROTOCOL)

    def ricercaOrdine(self, codiceOrdine):
        if os.path.isfile('Dati\Ordini.pickle'):
            with open('Dati\Ordini.pickle', 'rb') as f:
                ordini = dict(pickle.load(f))
                return ordini.get(codiceOrdine, None)
        else:
            raise Exception("Ordine non trovato")

    def stampaListaPiatti(self):
        stri = ""
        if os.path.isfile('Dati\Piatti.pickle'):
            with open('Dati\Piatti.pickle', 'rb') as f:
                menu = dict(pickle.load(f))
            for i in self.listaPiatti.keys():
                for piatto in menu.values():
                    if piatto.numero == i:
                        stri += str(self.listaPiatti[i]) + '  '+ piatto.nome+ '  ' + str(piatto.prezzo*self.listaPiatti[i]) +'€\n'
        return stri

    def __str__(self):
        return "Codice dell'ordine: % s \nStato dell'ordine: % s \nLista dei piatti: % s"%\
               (self.codice,self.statoOrdine,self.listaPiatti)