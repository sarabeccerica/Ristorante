import os
import pickle


class Piatto:

    def __init__(self):
        self.nome = ""
        self.numero = 0
        self.prezzo = 0

    def aggiungiPiatto(self,nome,prezzo,numeroPiatto):
        piatti = {}
        if os.path.isfile('Dati\Piatti.pickle'):
            with open('Dati\Piatti.pickle', 'rb') as f:
                piatti = dict(pickle.load(f))
        if not(numeroPiatto in piatti.keys()) and self.controlloNumeroPiatto(numeroPiatto) and self.controlloPrezzo(prezzo):
            self.numero = numeroPiatto
            self.prezzo = prezzo
            self.nome = nome
            piatti[numeroPiatto] = self
            with open('Dati\Piatti.pickle', 'wb') as f:
                pickle.dump(piatti, f, pickle.HIGHEST_PROTOCOL)
        else:
            raise Exception("Numero piatto già presente nel menu")

    def controlloNumeroPiatto(self,numeroPiatto):
        if numeroPiatto<=0:
            raise Exception("Controlla di aver inserito un numero per il piatto valido")
        return True

    def controlloPrezzo(self,prezzo):
        if prezzo<=0:
            raise Exception("Controlla di aver inserito un prezzo valido")
        return True

    def ricercaPiatto(self,numeroPiatto):
        if os.path.isfile('Dati\Piatti.pickle'):
            with open('Dati\Piatti.pickle', 'rb') as f:
                piatti = dict(pickle.load(f))
            for piatto in piatti.values():
                if piatto.numero == numeroPiatto:
                    return piatto
        raise Exception("Piatto non presente nel menu")

    def eliminaPiatto(self,numeroPiatto):
        piatti = {}
        if os.path.isfile('Dati\Piatti.pickle'):
            with open('Dati\Piatti.pickle', 'rb') as f:
                piatti = pickle.load(f)
                try:
                    del piatti[numeroPiatto]
                except:
                    raise Exception("Piatto non trovato")
        with open('Dati\Piatti.pickle', 'wb') as f:
            pickle.dump(piatti, f, pickle.HIGHEST_PROTOCOL)
        self.nome = ""
        self.prezzo = 0
        self.numero = 0
        del self

    def modificaPiatto(self,nome, prezzo, numeroPiatto):
        if os.path.isfile('Dati\Piatti.pickle'):
            with open('Dati\Piatti.pickle', 'rb') as f:
                piatti = pickle.load(f)
                piatti[numeroPiatto].nome = nome
                piatti[numeroPiatto].prezzo = prezzo
                self.controlloPrezzo(prezzo)
            with open('Dati\Piatti.pickle', 'wb') as f:
                pickle.dump(piatti, f, pickle.HIGHEST_PROTOCOL)

    def __str__(self):
        return "Numero del piatto: % s \nNome: % s \nPrezzo: % s€"%(self.numero,self.nome,self.prezzo)