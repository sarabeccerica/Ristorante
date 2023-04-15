from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from Viste.Cameriere.VistaAssegnaConPrenotazione import VistaAssegnaConPrenotazione
from Viste.Cameriere.VistaAssegnaSenzaPrenotazione import VistaAssegnaSenzaPrenotazione


class VistaAssegnaTavoli(QWidget):

    def __init__(self,parent = None):
        super(VistaAssegnaTavoli, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_genericButton("Assegna tavoli con prenotazione", self.go_assegnaConPrenotazione), 0, 0)
        grid_layout.addWidget(self.get_genericButton("Assegna tavoli senza prenotazione", self.go_assegnaSenzaPrenotazione), 0, 1)
        button = QPushButton("Esci")
        button.setSizePolicy(20, QSizePolicy.Expanding)
        button.clicked.connect(self.go_esci)
        grid_layout.addWidget(button, 2, 0)
        grid_layout.setRowStretch(50, 50)
        self.setLayout(grid_layout)
        self.resize(400, 100)
        self.setWindowTitle("Assegna tavoli")

    def get_genericButton(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_assegnaConPrenotazione(self):
        self.vista_assegna_con_pren = VistaAssegnaConPrenotazione()
        self.vista_assegna_con_pren.show()

    def go_assegnaSenzaPrenotazione(self):
        self.vista_assegna_senza_pren = VistaAssegnaSenzaPrenotazione()
        self.vista_assegna_senza_pren.show()

    def go_esci(self):
        self.close()