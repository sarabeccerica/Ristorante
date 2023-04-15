import datetime
import os
import pickle
import time

class Prenotazione:

    def __init__(self):
        self.dataOra = datetime.datetime(year = 1970, month = 1, day = 1)
        self.nome = ""
        self.numeroPersone = 0
        self.tavoliAssociati = []

    def aggiungiPrenotazione(self, dataOra, nome, numeroPersone):
        if self.controlloData(dataOra) and self.controlloNome(nome) and self.controlloNumeroPersone(numeroPersone):
            i = list(self.verificaDisponibilita(dataOra, numeroPersone))
            if len(i):
                self.tavoliAssociati = list(i)
                self.dataOra = dataOra
                self.nome = nome
                self.numeroPersone = numeroPersone
                prenotazioni = {}
                if os.path.isfile('Dati\Prenotazioni.pickle'):
                    with open('Dati\Prenotazioni.pickle', 'rb') as f:
                        prenotazioni = dict(pickle.load(f))
                prenotazioni[nome] = self
                with open('Dati\Prenotazioni.pickle', 'wb') as f:
                    pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)

    def modificaPrenotazione(self,dataOra, nome, numeroPersone):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
                prenotazioni[nome].dataOra = dataOra
                prenotazioni[nome].numeroPersone = numeroPersone
                self.controlloNumeroPersone(numeroPersone)
                self.controlloData(dataOra)
            with open('Dati\Prenotazioni.pickle', 'wb') as f:
                pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)

    def verificaDisponibilita(self, dataOra, numeroPersone):
        tavoliAssociati = {}
        tavoli = {}
        prenotazioni = {}
        if os.path.isfile('Dati\Tavoli.pickle'):
            with open('Dati\Tavoli.pickle', 'rb') as f:
                tavoli = dict(pickle.load(f))
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
                for prenotazione in prenotazioni.values():
                    if time.mktime(dataOra.timetuple()) - time.mktime(prenotazione.dataOra.timetuple()) >= -3600 and \
                            time.mktime(dataOra.timetuple()) - time.mktime(prenotazione.dataOra.timetuple()) <= 3600:
                        for tavolo in prenotazione.tavoliAssociati:
                            try:
                                del tavoli[tavolo.numero]
                            except:
                                raise Exception("Tavoli insufficenti")
        if numeroPersone % 6 != 0:
            tavoliNecessari = int(numeroPersone/6)+1
        else:
            tavoliNecessari = int(numeroPersone/6)
        if len(tavoli)>= tavoliNecessari:
            while tavoliNecessari>0:
                chiavi = list(tavoli.keys())
                tavoliAssociati[tavoli[chiavi[0]]] = tavoli[chiavi[0]]
                del tavoli[chiavi[0]]
                tavoliNecessari-=1
        return tavoliAssociati

    def eliminaPrenotazione(self,nome):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
                try:
                    del prenotazioni[nome]
                except:
                    raise Exception("Prenotazione non trovata")
            with open('Dati\Prenotazioni.pickle', 'wb') as f:
                pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
        self.dataOra = datetime.datetime(year=1970, month=1, day=1)
        self.nome = ""
        self.numeroPersone = 0
        self.tavoliAssociati = {}
        del self

    def ricercaPrenotazione(self, nome):
        prenotazioni = {}
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
        for chiave in prenotazioni.keys():
            if chiave == nome:
                return prenotazioni[chiave]
        raise Exception("Prenotazione non trovata")

    def stampaTavoliAssociati(self):
        stri = ""
        for tavolo in self.tavoliAssociati:
            stri += tavolo.__str__()
        return stri

    def arrivoPrenotati(self, nomePrenotazione):
        prenotazione = self.ricercaPrenotazione(nomePrenotazione)
        if time.mktime(datetime.datetime.now().timetuple()) - time.mktime(prenotazione.dataOra.timetuple()) >= -1800 and \
                time.mktime(datetime.datetime.now().timetuple()) - time.mktime(prenotazione.dataOra.timetuple()) <= 1800:
            for tavolo in prenotazione.tavoliAssociati:
                tavolo.modificaStatoTavolo(tavolo.numero, "Occupato")
            return prenotazione.tavoliAssociati
        raise Exception("Prenotazione non attiva")

    def controlloData(self, data):
        if time.mktime(data.timetuple()) >= time.mktime(datetime.datetime.now().timetuple()) and \
                ((data.hour >= 12 and data.hour <=14) or (data.hour >= 17 and data.hour <= 21)) and data.weekday() !=0\
                and ((data.timetuple().tm_yday < 274) or (data.timetuple().tm_yday >288)) :
            return True
        raise Exception("Controlla di aver inserito correttamente la data e l'ora")

    def controlloNumeroPersone(self, numeroP):
        if numeroP<=0:
            raise Exception("Controlla di aver inserito correttamente il numero di persone")
        return True

    def controlloNome(self,nome):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
            for chiave in prenotazioni.keys():
                if chiave == nome:
                    raise Exception("Controlla di aver inserito correttamente il nome della prenotazione")
        return True

    def __str__(self):
        return "Nome: % s\nData: % s\nNumero persone: % r\n Tavoli associati: % s\n" % (self.nome, self.dataOra,
                                                                                self.numeroPersone,self.stampaTavoliAssociati())