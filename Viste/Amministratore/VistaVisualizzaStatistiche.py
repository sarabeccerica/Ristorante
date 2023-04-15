from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from Viste.Amministratore.VistaStatistichePrenotazioni import VistaStatistichePrenotazioni
from Viste.Amministratore.VistaStatisticheScontrini import VistaStatisticheScontrini


class VistaVisualizzaStatistiche(QWidget):

    def __init__(self, parent = None):
        super(VistaVisualizzaStatistiche, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_genericButton("Statistiche Prenotazioni", self.go_statistichePrenotazioni), 0, 0)
        grid_layout.addWidget(self.get_genericButton("Statistiche Scontrini", self.go_statisticheScontrini), 0, 1)
        grid_layout.addWidget(self.get_genericButton("Indietro", self.go_indietro), 1, 0)
        grid_layout.setRowStretch(50, 50)
        self.setLayout(grid_layout)
        self.resize(400, 90)
        self.setWindowTitle("Visualizza Statistiche")

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_statistichePrenotazioni(self):
        self.vista_statistiche_prenotazioni = VistaStatistichePrenotazioni()
        self.vista_statistiche_prenotazioni.show()

    def go_statisticheScontrini(self):
        self.vista_statistiche_scontrini = VistaStatisticheScontrini()
        self.vista_statistiche_scontrini.show()

    def go_indietro(self):
        self.close()