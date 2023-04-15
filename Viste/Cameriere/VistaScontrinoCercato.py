from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy

from Gestione.Scontrino import Scontrino


class VistaScontrinoCercato(QWidget):
    def __init__(self,codice,callback):
        super(VistaScontrinoCercato, self).__init__()
        self.codice = codice
        self.callback = callback
        self.scontrino = Scontrino()
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(QLabel("Codice"), 0, 0)
        self.grid_layout.addWidget(QLabel(str(self.scontrino.ricercaScontrino(codice).codice)), 0, 1)
        self.grid_layout.addWidget(QLabel("Tavolo: "), 1, 0)
        self.grid_layout.addWidget(QLabel(str(self.scontrino.ricercaScontrino(codice).numeroTavolo)), 1, 1)
        self.grid_layout.addWidget(QLabel("Data: "), 2, 0)
        self.grid_layout.addWidget(QLabel(str(self.scontrino.ricercaScontrino(codice).dataOra)), 2, 1)
        self.grid_layout.addWidget(QLabel("Piatti: "), 3, 0)
        self.grid_layout.addWidget(QLabel(self.scontrino.ricercaScontrino(codice).stampaPiatti()), 3, 1)
        self.grid_layout.addWidget(QLabel("Totale: "), 4, 0)
        self.grid_layout.addWidget(QLabel(str(self.scontrino.ricercaScontrino(codice).totale)), 4, 1)
        self.grid_layout.addWidget(self.get_genericButton("Elimina scontrino", self.go_eliminaScontrino), 5, 1)
        self.grid_layout.addWidget(self.get_genericButton("Indietro", self.indietro), 5, 0)
        self.setLayout(self.grid_layout)
        self.setWindowTitle("Scontrino")

    def get_genericButton(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def indietro(self):
        self.close()

    def go_eliminaScontrino(self):
        self.scontrino.eliminaScontrino(self.codice)
        self.callback()
        self.close()