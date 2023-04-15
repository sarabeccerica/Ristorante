import os
import pickle
from Servizio.Dipendente import Dipendente


class Cameriere(Dipendente):

    def __init__(self):
        super().__init__()

    def aggiungiCameriere(self, nome, cognome, dataNascita, codiceFiscale, email, password, telefono):
        self.aggiungiDipendente(nome=nome, cognome=cognome, dataNascita=dataNascita, codiceFiscale=codiceFiscale,
                            email=email, password=password, telefono=telefono)
        camerieri = {}
        if os.path.isfile('Dati\Camerieri.pickle'):
            with open('Dati\Camerieri.pickle', 'rb') as f:
                camerieri = dict(pickle.load(f))
        camerieri[codiceFiscale] = self
        with open('Dati\Camerieri.pickle', 'wb') as f:
            pickle.dump(camerieri, f, pickle.HIGHEST_PROTOCOL)

    def getDatiCameriere(self):
        info = self.getDatiDipendente()
        return info

    def modificaCameriere(self, nome, cognome, dataNascita, codiceFiscale, email, password, telefono):
        if os.path.isfile('Dati\Camerieri.pickle'):
            with open('Dati\Camerieri.pickle', 'rb') as f:
                camerieri = dict(pickle.load(f))
                try:
                    del camerieri[codiceFiscale]
                except:
                    raise Exception("Cameriere non trovato")
        self.aggiungiCameriere(nome, cognome, dataNascita, codiceFiscale, email, password, telefono)

    def notificaDipendente(self, ordine):
        messaggiCuoco = {}
        stri = ""
        if os.path.isfile('Dati\MessaggiCuoco.pickle'):
            with open('Dati\MessaggiCuoco.pickle', 'rb') as f:
                messaggiCuoco = dict(pickle.load(f))
        stri += "Preparare ordine: "+ str(ordine.codice)
        listaP = dict(ordine.listaPiatti)
        for i in listaP.keys():
            stri += "  -Piatto: "+ str(i)+ " Prozioni: "
            for j in listaP.values():
                if j == listaP[i]:
                    stri += str(j)
        messaggiCuoco[ordine.codice] = stri
        with open('Dati\MessaggiCuoco.pickle', 'wb') as f:
            pickle.dump(messaggiCuoco, f, pickle.HIGHEST_PROTOCOL)

    def ordineConsegnato(self,ordine):
        if os.path.isfile('Dati\MessaggiCameriere.pickle'):
            with open('Dati\MessaggiCameriere.pickle', 'rb') as f:
                messaggiCameriere = dict(pickle.load(f))
                try:
                    del messaggiCameriere[ordine.codice]
                    ordine.ordineConsegnato(ordine.codice)
                except:
                    raise Exception("Ordine non trovato")
        with open('Dati\MessaggiCameriere.pickle', 'wb') as f:
            pickle.dump(messaggiCameriere, f, pickle.HIGHEST_PROTOCOL)

    def visualizzaListaMessaggi(self):
        if os.path.isfile('Dati\MessaggiCameriere.pickle'):
            with open('Dati\MessaggiCameriere.pickle', 'rb') as f:
                messaggiCameriere = dict(pickle.load(f))
                return messaggiCameriere
        else:
            raise Exception("Errore")

    def verificaCredenziali(self, codiceFiscale, password):
        if os.path.isfile('Dati\Camerieri.pickle'):
            with open('Dati\Camerieri.pickle', 'rb') as f:
                camerieri = dict(pickle.load(f))
            for cameriere in camerieri.values():
                if cameriere.codiceFiscale == codiceFiscale and cameriere.password == password:
                    return True

    def ricercaDipendente(self, codiceFiscale):
        if os.path.isfile('Dati\Camerieri.pickle'):
            with open('Dati\Camerieri.pickle', 'rb') as f:
                camerieri = dict(pickle.load(f))
                return camerieri.get(codiceFiscale, None)
        else:
            raise Exception("Cameriere non trovato")

    def eliminaCameriere(self,codiceFiscale):
        if os.path.isfile('Dati\Camerieri.pickle'):
            with open('Dati\Camerieri.pickle', 'rb') as f:
                camerieri = dict(pickle.load(f))
                try:
                    del camerieri[codiceFiscale]
                except:
                    raise Exception("Cameriere non trovato")
            with open('Dati\Camerieri.pickle', 'wb') as f:
                pickle.dump(camerieri, f, pickle.HIGHEST_PROTOCOL)
        self.rimuoviDipendente()
        del self

