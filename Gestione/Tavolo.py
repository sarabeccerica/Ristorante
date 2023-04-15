import os
import pickle

class Tavolo:

    def __init__(self):
        self.stato = ""
        self.numero = 0

    def aggiungiTavolo(self):
        tavoli = {}
        t = 1
        if os.path.isfile('Dati\Tavoli.pickle'):
            with open('Dati\Tavoli.pickle', 'rb') as f:
                tavoli = dict(pickle.load(f))
                for tavolo in tavoli.values():
                    if tavolo.numero >= t:
                        t = tavolo.numero + 1
        self.numero = t
        self.stato = "Libero"
        tavoli[t] = self
        with open('Dati\Tavoli.pickle', 'wb') as f:
            pickle.dump(tavoli, f, pickle.HIGHEST_PROTOCOL)

    def ricercaTavolo(self,numeroTavolo):
        if os.path.isfile('Dati\Tavoli.pickle'):
            with open('Dati\Tavoli.pickle', 'rb') as f:
                tavoli = dict(pickle.load(f))
                return tavoli.get(numeroTavolo, None)
        else:
            raise Exception("Tavolo non trovato")

    def eliminaTavolo(self, numero):
        if os.path.isfile('Dati\Tavoli.pickle'):
            with open('Dati\Tavoli.pickle', 'rb') as f:
                tavoli = pickle.load(f)
                try:
                    del tavoli[numero]
                except:
                    raise Exception("Tavolo non trovato")
            with open('Dati\Tavoli.pickle', 'wb') as f:
                pickle.dump(tavoli, f, pickle.HIGHEST_PROTOCOL)
        self.stato = ""
        self.numero = 0
        del self

    def modificaStatoTavolo(self, numeroTavolo, nuovoStato):
        tavoli = {}
        if os.path.isfile('Dati\Tavoli.pickle'):
            with open('Dati\Tavoli.pickle', 'rb') as f:
                tavoli = pickle.load(f)
        for tavolo in tavoli.values():
            if tavolo.numero == numeroTavolo:
                tavolo.stato = nuovoStato
                with open('Dati\Tavoli.pickle', 'wb') as f:
                    pickle.dump(tavoli, f, pickle.HIGHEST_PROTOCOL)
                return
        raise Exception("Tavolo non trovato")

    def assegnaTavoloSenzaPrenotazione(self, quantitaTavoli):
        tavoli = {}
        tavoliAssegnati = {}
        if os.path.isfile('Dati\Tavoli.pickle'):
            with open('Dati\Tavoli.pickle', 'rb') as f:
                tavoli = pickle.load(f)
        contatore = 0
        for tavolo in tavoli.values():
            if tavolo.stato == "Libero":
                contatore+=1
        if contatore< quantitaTavoli:
            raise Exception("Tavoli Insufficenti")
        for tavolo in tavoli.values():
            if tavolo.stato == "Libero":
                self.modificaStatoTavolo(tavolo.numero, "Occupato")
                quantitaTavoli -=1
                tavolo.stato= "Occupato"
                tavoliAssegnati[tavolo.numero] = tavolo
            if quantitaTavoli == 0:
                return tavoliAssegnati
        raise Exception("Errore")

    def __str__(self):
        return "-Numero del tavolo: % s    Stato: % s   "%(self.numero,self.stato)

