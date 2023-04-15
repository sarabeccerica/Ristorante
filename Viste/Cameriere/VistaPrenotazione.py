from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy

from Gestione.Prenotazione import Prenotazione
from Viste.Cameriere.VistaModificaPrenotazione import VistaModificaPrenotazione


class VistaPrenotazione(QWidget):
    def __init__(self,nome,callback):
        super(VistaPrenotazione, self).__init__()
        self.nome = nome
        self.callback = callback
        self.prenotazione = Prenotazione()
        self.prenotazione.ricercaPrenotazione(str(self.nome))
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(QLabel("Nome: "),0,0)
        self.grid_layout.addWidget(QLabel(self.prenotazione.ricercaPrenotazione(str(self.nome)).nome),0,1)
        #self.grid_layout.addWidget(QLabel("Tavoli: "),1,0)
        #self.grid_layout.addWidget(QLabel(self.prenotazione.ricercaPrenotazione(str(self.nome)).stampaTavoliAssociati()),1,1)
        self.grid_layout.addWidget(QLabel("Data: "),2,0)
        self.grid_layout.addWidget(QLabel(str(self.prenotazione.ricercaPrenotazione(str(self.nome)).dataOra)),2,1)
        self.grid_layout.addWidget(QLabel("Numero persone: "),3,0)
        self.grid_layout.addWidget(QLabel(str(self.prenotazione.ricercaPrenotazione(str(self.nome)).numeroPersone)),3,1)
        self.grid_layout.addWidget(self.get_genericButton("Elimina prenotazione",self.go_eliminaPrenotazione),5,2)
        self.grid_layout.addWidget(self.get_genericButton("Modifica prenotazione", self.go_modificaPrenotazione), 5, 1)
        self.grid_layout.addWidget(self.get_genericButton("Indietro",self.indietro),5,0)
        self.setLayout(self.grid_layout)
        self.setWindowTitle("Prenotazione")


    def get_genericButton(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def indietro(self):
        self.close()

    def go_modificaPrenotazione(self):
        self.vista_modifica_prenotazione = VistaModificaPrenotazione(nomeP =self.nome,callback = self.callback)
        self.vista_modifica_prenotazione.show()
        self.close()

    def go_eliminaPrenotazione(self):
        self.prenotazione.eliminaPrenotazione(self.nome)
        self.callback()
        self.close()
