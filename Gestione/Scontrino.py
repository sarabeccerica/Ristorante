import datetime
import os
import pickle

class Scontrino:

    def __init__(self):
        self.codice = 0
        self.dataOra = datetime.datetime(year= 1970, month=1, day=1)
        self.numeroTavolo= 0
        self.ordiniAssociati = []
        self.totale = 0

    def aggiungiScontrino(self, numeroTavolo):
        codice = 1
        scontrini = {}
        self.dataOra = datetime.date.today()
        self.numeroTavolo = numeroTavolo
        self.liberaTavolo(self.numeroTavolo)
        self.ordiniAssociati = self.associaOrdini(numeroTavolo)
        self.totale = self.calcoloTotale(self.ordiniAssociati)
        if os.path.isfile('Dati\Scontrini.pickle'):
            with open('Dati\Scontrini.pickle', 'rb') as f:
                scontrini = dict(pickle.load(f))
                for i in scontrini.keys():
                    if i >= codice:
                        codice = i+1
        self.codice = codice
        scontrini[codice] = self
        with open('Dati\Scontrini.pickle', 'wb') as f:
            pickle.dump(scontrini, f, pickle.HIGHEST_PROTOCOL)

    def liberaTavolo(self,numeroTavolo):
        tavoli = {}
        if os.path.isfile('Dati\Tavoli.pickle'):
            with open('Dati\Tavoli.pickle', 'rb') as f:
                tavoli = pickle.load(f)
        for tavolo in tavoli.values():
            if tavolo.numero == numeroTavolo:
                tavolo.modificaStatoTavolo(numeroTavolo,"Libero")

    def associaOrdini(self, numeroTavolo):
        ordiniAssociati = []
        if os.path.isfile('Dati\Ordini.pickle'):
            with open('Dati\Ordini.pickle', 'rb') as f:
                ordini = dict(pickle.load(f))
                for i in ordini.keys():
                    if int(i/100) == numeroTavolo:
                        ordiniAssociati.append(ordini[i])
                for ordine in ordiniAssociati:
                    if ordine.statoOrdine != "Consegnato":
                        raise Exception("Ordine ancora in fase di "+str(ordine.statoOrdine))
                    del ordini[ordine.codice]
            with open('Dati\Ordini.pickle', 'wb') as f:
                pickle.dump(ordini, f, pickle.HIGHEST_PROTOCOL)
        return ordiniAssociati

    def calcoloTotale(self, ordiniScontrino):
        totale = 0
        if os.path.isfile('Dati\Piatti.pickle'):
            with open('Dati\Piatti.pickle', 'rb') as f:
                piatti = dict(pickle.load(f))
        for ordine in ordiniScontrino:
            listaPiatti = dict(ordine.listaPiatti)
            for chiave in listaPiatti.keys():
                for piatto in piatti.values():
                    if chiave == piatto.numero:
                        totale += piatto.prezzo * listaPiatti[chiave]
        return totale

    def eliminaScontrino(self,codice):
        scontrini = {}
        if os.path.isfile('Dati\Scontrini.pickle'):
            with open('Dati\Scontrini.pickle', 'rb') as f:
                scontrini = dict(pickle.load(f))
                try:
                    del scontrini[codice]
                except:
                    raise Exception("Scontrino non trovato")
        with open('Dati\Scontrini.pickle', 'wb') as f:
            pickle.dump(scontrini, f, pickle.HIGHEST_PROTOCOL)
        self.codice = 0
        self.dataOra = datetime.datetime(year=1970, month=1, day=1)
        self.numeroTavolo = 0
        self.ordiniAssociati = []
        self.totale = 0
        del self

    def ricercaScontrino(self, codice):
        scontrini = {}
        if os.path.isfile('Dati\Scontrini.pickle'):
            with open('Dati\Scontrini.pickle', 'rb') as f:
                scontrini = dict(pickle.load(f))
        for i in scontrini.keys():
            if i == codice:
                return scontrini[i]
        raise Exception("Scontrino non trovato")

    def stampaPiatti(self):
        stri = ""
        for ordine in self.ordiniAssociati:
            stri += ordine.stampaListaPiatti()
        return stri

    def __str__(self):
        return "Codice: % s\nData: % s\nNumero tavolo: % r\n% s\nTotale: % s€\n" % (self.codice, self.dataOra,
                                                            self.numeroTavolo,self.stampaPiatti(),self.totale)