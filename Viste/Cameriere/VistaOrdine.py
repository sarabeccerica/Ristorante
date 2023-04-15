from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy

from Gestione.Ordine import Ordine

class VistaOrdine(QWidget):
    def __init__(self,codice):
        super(VistaOrdine, self).__init__()
        self.codice = codice
        self.ordine = Ordine()
        self.ordine.ricercaOrdine(int(self.codice))
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(QLabel("Codice: "),0,0)
        self.grid_layout.addWidget(QLabel(str(self.ordine.ricercaOrdine(int(self.codice)).codice)),0,1)
        self.grid_layout.addWidget(QLabel("Stato ordine: "),1,0)
        self.grid_layout.addWidget(QLabel(self.ordine.ricercaOrdine(int(self.codice)).statoOrdine),1,1)
        self.grid_layout.addWidget(QLabel("Lista piatti: "),2,0)
        self.grid_layout.addWidget(QLabel(self.ordine.ricercaOrdine(int(self.codice)).stampaListaPiatti()),2,1)
        self.grid_layout.addWidget(self.get_genericButton("Indietro",self.indietro),5,0)
        self.setLayout(self.grid_layout)
        self.setWindowTitle("Ordine")

    def get_genericButton(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def indietro(self):
        self.close()
