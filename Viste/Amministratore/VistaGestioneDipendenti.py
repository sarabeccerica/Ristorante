from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QGridLayout

from Viste.Amministratore.VistaAggiungiCameriere import VistaAggiungiCameriere
from Viste.Amministratore.VistaAggiungiCuoco import VistaAggiungiCuoco
from Viste.Amministratore.VistaRicercCameriere import VistaRicercCameriere
from Viste.Amministratore.VistaRicercaCuoco import VistaRicercaCuoco
from Viste.Amministratore.VistaVisualizzaDipendenti import VistaVisualizzaDipendenti


class VistaGestioneDipendenti(QWidget):

    def __init__(self, parent = None):
        super(VistaGestioneDipendenti, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_genericButton("Aggiungi cuoco", self.go_aggiungiCuoco), 0, 0)
        grid_layout.addWidget(self.get_genericButton("Cerca cuoco", self.go_cercaCuoco), 0, 1)
        grid_layout.addWidget(self.get_genericButton("Aggiungi cameriere", self.go_aggiungiCameriere), 1, 0)
        grid_layout.addWidget(self.get_genericButton("Cerca cameriere", self.go_cercaCameriere), 1, 1)
        grid_layout.addWidget(self.get_genericButton("Visualizza dipendenti", self.go_visualizzaDipendenti), 2, 1)
        button = QPushButton("Indietro")
        button.setSizePolicy(20, QSizePolicy.Expanding)
        button.clicked.connect(self.go_GestioneAmministratore)
        grid_layout.addWidget(button, 2, 0)
        grid_layout.setRowStretch(50, 50)
        self.setLayout(grid_layout)
        self.resize(400, 100)
        self.setWindowTitle("Gestione dipendenti")

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_aggiungiCuoco(self):
        self.vista_aggiungi_cuoco = VistaAggiungiCuoco()
        self.vista_aggiungi_cuoco.show()


    def go_aggiungiCameriere(self):
        self.vista_aggiungi_cameriere = VistaAggiungiCameriere()
        self.vista_aggiungi_cameriere.show()

    def go_cercaCuoco(self):
        self.vista_ricerca_cuoco = VistaRicercaCuoco()
        self.vista_ricerca_cuoco.show()

    def go_cercaCameriere(self):
        self.vista_ricerca_cameriere = VistaRicercCameriere()
        self.vista_ricerca_cameriere.show()

    def go_visualizzaDipendenti(self):
        self.vista_visualizza_dipendenti = VistaVisualizzaDipendenti()
        self.vista_visualizza_dipendenti.show()

    def go_GestioneAmministratore(self):
        self.close()
