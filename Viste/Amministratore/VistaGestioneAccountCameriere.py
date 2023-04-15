from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy

from Servizio.Cameriere import Cameriere


class VistaGestioneAccountCameriere(QWidget):
    def __init__(self,cf):
        super(VistaGestioneAccountCameriere, self).__init__()
        self.cf = cf
        self.cameriere = Cameriere()
        self.cameriere.ricercaDipendente(str(self.cf))
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(QLabel("Nome: "),0,0)
        self.grid_layout.addWidget(QLabel(self.cameriere.ricercaDipendente(str(self.cf)).nome),0,1)
        self.grid_layout.addWidget(QLabel("Cognome: "),1,0)
        self.grid_layout.addWidget(QLabel(self.cameriere.ricercaDipendente(str(self.cf)).cognome),1,1)
        self.grid_layout.addWidget(QLabel("Data: "),2,0)
        self.grid_layout.addWidget(QLabel(str(self.cameriere.ricercaDipendente(str(self.cf)).dataNascita)),2,1)
        self.grid_layout.addWidget(QLabel("Email: "),3,0)
        self.grid_layout.addWidget(QLabel(self.cameriere.ricercaDipendente(str(self.cf)).email),3,1)
        self.grid_layout.addWidget(QLabel("Codice fiscale: "),4,0)
        self.grid_layout.addWidget(QLabel(self.cameriere.ricercaDipendente(str(self.cf)).codiceFiscale),4,1)
        self.grid_layout.addWidget(QLabel("Numero di telefono: "),5,0)
        self.grid_layout.addWidget(QLabel(self.cameriere.ricercaDipendente(str(self.cf)).telefono),5,1)
        self.grid_layout.addWidget(self.get_genericButton("Elimina account",self.go_eliminaCameriere),6,1)
        self.grid_layout.addWidget(self.get_genericButton("Indietro",self.indietro),6,0)
        self.setLayout(self.grid_layout)
        self.setWindowTitle("Account")

    def get_genericButton(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def indietro(self):
        self.close()

    def go_eliminaCameriere(self):
        self.cameriere.eliminaCameriere(self.cf)
        self.close()
