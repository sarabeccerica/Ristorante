from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy

from Sistema.Piatto import Piatto
from Viste.Amministratore.VistaModificaPiatto import VistaModificaPiatto


class VistaEliminaPiatto(QWidget):
    def __init__(self,callback, numeroPiatto):
        super(VistaEliminaPiatto, self).__init__()
        self.callback = callback
        self.numeroPiatto = numeroPiatto
        self.piatto1 = Piatto()
        self.piatto = self.piatto1.ricercaPiatto(int(self.numeroPiatto))
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(QLabel("Nome: "),0,0)
        self.grid_layout.addWidget(QLabel(self.piatto.nome),0,1)
        self.grid_layout.addWidget(QLabel("Numero: "),1,0)
        self.grid_layout.addWidget(QLabel(str(self.piatto.numero)),1,1)
        self.grid_layout.addWidget(QLabel("Prezzo: "),2,0)
        self.grid_layout.addWidget(QLabel(str(self.piatto.prezzo)),2,1)
        self.grid_layout.addWidget(self.get_genericButton("Elimina piatto",self.go_eliminaPiatto),3,2)
        self.grid_layout.addWidget(self.get_genericButton("Modifica piatto", self.go_modificaPiatto), 3, 1)
        self.grid_layout.addWidget(self.get_genericButton("Indietro",self.indietro),3,0)
        self.setLayout(self.grid_layout)
        self.setWindowTitle("Piatto")

    def get_genericButton(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def indietro(self):
        self.close()

    def go_modificaPiatto(self):
        self.vista_modifica_piatto = VistaModificaPiatto(numero = self.piatto.numero,callback = self.callback)
        self.vista_modifica_piatto.show()
        self.close()

    def go_eliminaPiatto(self):
        self.piatto1.eliminaPiatto(self.numeroPiatto)
        self.callback()
        self.close()