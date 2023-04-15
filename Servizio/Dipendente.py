import datetime
from abc import abstractmethod


class Dipendente:

    def __init__(self):
        self.nome = ""
        self.cognome = ""
        self.dataNascita = datetime.datetime(year=1970, month=1, day=1)
        self.codiceFiscale = ""
        self.email = ""
        self.password = ""
        self.telefono = ""
        self.listaMessaggi = []

    def aggiungiDipendente(self, nome, cognome, dataNascita, codiceFiscale, email, password, telefono):
        self.nome = nome
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.codiceFiscale = codiceFiscale
        self.email = email
        self.password = password
        self.telefono = telefono

    def getDatiDipendente(self):
        return {
            "nome": self.nome,
            "cognome": self.cognome,
            "dataNascita": self.dataNascita,
            "codiceFiscale": self.codiceFiscale,
            "email": self.email,
            "telefono": self.telefono
        }

    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getDataNascita(self):
        return self.dataNascita

    def getCodiceFiscale(self):
        return self.codiceFiscale

    def getEmail(self):
        return self.email

    def getTelefono(self):
        return self.telefono

    def rimuoviDipendente(self):
        self.nome = ""
        self.cognome = ""
        self.dataNascita = datetime.datetime(year=1970, month=1, day=1)
        self.codiceFiscale = ""
        self.email = ""
        self.password = ""
        self.telefono = ""

    def __str__(self):
        return "Nome: % s\nCognome: % s \nData di nascita: % s \nCodice fiscale: % s \nEmail: %" \
               "s \nTelefono: % s" % (self.nome, self.cognome, self.dataNascita, self.codiceFiscale,
                                      self.email, self.telefono)
    @abstractmethod
    def verificaCredenziali(self, codiceFiscale, password):
        pass

    @abstractmethod
    def notificaDipendente(self):
        pass

    @abstractmethod
    def ricercaDipendente(self, codiceFiscale):
        pass

    @abstractmethod
    def visualizzaListaMessaggi(self):
        pass


