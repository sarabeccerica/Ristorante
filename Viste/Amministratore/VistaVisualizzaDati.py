from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QSizePolicy

from Viste.Amministratore.VistaVisualizzaPrenotazioni import VistaVisualizzaPrenotazioni
from Viste.Amministratore.VistaVisualizzaScontrini import VistaVisualizzaScontrini


class VistaVisualizzaDati(QWidget):

    def __init__(self, parent = None):
        super(VistaVisualizzaDati, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_genericButton("Visualizza Scontrini", self.go_visualizzaScontrini),0,0)
        grid_layout.addWidget(self.get_genericButton("Visualizza Prenotazioni", self.go_visualizzaPrenotazioni),0,1)
        grid_layout.addWidget(self.get_genericButton("Indietro", self.go_indietro),1,0)
        grid_layout.setRowStretch(50, 50)
        self.setLayout(grid_layout)
        self.resize(400, 90)
        self.setWindowTitle("Visualizza Dati")


    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_visualizzaScontrini(self):
        self.vista_visualizza_scontrini = VistaVisualizzaScontrini()
        self.vista_visualizza_scontrini.show()

    def go_visualizzaPrenotazioni(self):
        self.vista_visualizza_prenotazioni = VistaVisualizzaPrenotazioni()
        self.vista_visualizza_prenotazioni.show()

    def go_indietro(self):
        self.close()