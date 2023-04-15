import os
import pickle
from Servizio.Dipendente import Dipendente


class Cuoco(Dipendente):

    def __init__(self):
        super().__init__()

    def aggiungiCuoco(self, nome, cognome, dataNascita, codiceFiscale, email, password, telefono):
        self.aggiungiDipendente(nome=nome, cognome=cognome, dataNascita=dataNascita, codiceFiscale=codiceFiscale,
                            email=email, password=password, telefono=telefono)
        cuochi = {}
        if os.path.isfile('Dati\Cuochi.pickle'):
            with open('Dati\Cuochi.pickle', 'rb') as f:
                cuochi = dict(pickle.load(f))
        cuochi[codiceFiscale] = self
        with open('Dati\Cuochi.pickle', 'wb') as f:
            pickle.dump(cuochi, f, pickle.HIGHEST_PROTOCOL)

    def modificaCuoco(self, nome, cognome, dataNascita, codiceFiscale, email, password, telefono):
        if os.path.isfile('Dati\Cuochi.pickle'):
            with open('Dati\Cuochi.pickle', 'rb') as f:
                cuochi = dict(pickle.load(f))
                try:
                    del cuochi[self.codiceFiscale]
                except:
                    raise Exception("Cuoco non trovato")
        self.aggiungiCuoco(nome, cognome, dataNascita, codiceFiscale, email, password, telefono)

    def notificaDipendente(self, ordine):
        messaggiCameriere = {}
        if os.path.isfile('Dati\MessaggiCameriere.pickle'):
            with open('Dati\MessaggiCameriere.pickle', 'rb') as f:
                messaggiCameriere = dict(pickle.load(f))
        messaggiCameriere[ordine.codice] = "Consegnare ordine: ", ordine.codice
        ordine.ordinePreparato(ordine.codice)
        with open('Dati\MessaggiCameriere.pickle', 'wb') as f:
            pickle.dump(messaggiCameriere, f, pickle.HIGHEST_PROTOCOL)
        if os.path.isfile('Dati\MessaggiCuoco.pickle'):
            with open('Dati\MessaggiCuoco.pickle', 'rb') as f:
                messaggiCuoco = dict(pickle.load(f))
        del messaggiCuoco[ordine.codice]
        with open('Dati\MessaggiCuoco.pickle', 'wb') as f:
            pickle.dump(messaggiCuoco, f, pickle.HIGHEST_PROTOCOL)

    def visualizzaListaMessaggi(self):
        if os.path.isfile('Dati\MessaggiCuoco.pickle'):
            with open('Dati\MessaggiCuoco.pickle', 'rb') as f:
                messaggiCuoco = dict(pickle.load(f))
            return messaggiCuoco
        else:
            raise Exception("Errore")

    def verificaCredenziali(self, codiceFiscale, password):
        if os.path.isfile('Dati\Cuochi.pickle'):
            with open('Dati\Cuochi.pickle', 'rb') as f:
                cuochi = dict(pickle.load(f))
            for cuoco in cuochi.values():
                if cuoco.codiceFiscale == codiceFiscale and cuoco.password == password:
                    return True

    def ricercaDipendente(self, codiceFiscale):
        if os.path.isfile('Dati\Cuochi.pickle'):
            with open('Dati\Cuochi.pickle', 'rb') as f:
                cuochi = dict(pickle.load(f))
                return cuochi.get(codiceFiscale, None)
        else:
            raise Exception("Cuoco non trovato")

    def eliminaCuoco(self,codiceFiscale):
        if os.path.isfile('Dati\Cuochi.pickle'):
            with open('Dati\Cuochi.pickle', 'rb') as f:
                cuochi = dict(pickle.load(f))
                try:
                    del cuochi[codiceFiscale]
                except:
                    raise Exception("Cuoco non trovato")
            with open('Dati\Cuochi.pickle', 'wb') as f:
                pickle.dump(cuochi, f, pickle.HIGHEST_PROTOCOL)
        self.rimuoviDipendente()
        del self