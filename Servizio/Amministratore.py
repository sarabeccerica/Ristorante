import os
import pickle

class Amministratore:

    def __init__(self):
        self.username = ""
        self.password = ""

    def aggiungiAmministratore(self,username,password):
        amministratori = {}
        if os.path.isfile('Dati\Amministratori.pickle'):
            with open('Dati\Amministratori.pickle', 'rb') as f:
                amministratori = dict(pickle.load(f))
        self.username = username
        self.password = password
        amministratori[username] = self
        with open('Dati\Amministratori.pickle', 'wb') as f:
            pickle.dump(amministratori, f, pickle.HIGHEST_PROTOCOL)

    def setPassword(self,username, passwordVecchia, passwordNuova):
        if os.path.isfile('Dati\Amministratori.pickle'):
            with open('Dati\Amministratori.pickle', 'rb') as f:
                amministratori = dict(pickle.load(f))
                for amministratore in amministratori.values():
                    if self.verificaCredenziali(username,passwordVecchia):
                        amministratore.password = passwordNuova
        with open('Dati\Amministratori.pickle', 'wb') as f:
            pickle.dump(amministratori, f, pickle.HIGHEST_PROTOCOL)

    def verificaCredenziali(self, username, password):
        if os.path.isfile('Dati\Amministratori.pickle'):
            with open('Dati\Amministratori.pickle', 'rb') as f:
                amministratori = dict(pickle.load(f))
            for amministratore in amministratori.values():
                if amministratore.username == username and amministratore.password == password:
                    return True

    def __str__(self):
        return "Username: % s \n pwd: % s"%(self.username,self.password)
