from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from Viste.Amministratore.VistaGestioneDipendenti import VistaGestioneDipendenti
from Viste.Amministratore.VistaGestioneMenu import VistaGestioneMenu
from Viste.Amministratore.VistaVisualizzaDati import VistaVisualizzaDati
from Viste.Amministratore.VistaVisualizzaStatistiche import VistaVisualizzaStatistiche


class VistaGestioneAmministratore(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneAmministratore,self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_genericButton("Gestione dipendenti", self.go_dipendenti), 0, 0)
        grid_layout.addWidget(self.get_genericButton("Visualizza statistiche", self.go_statistiche), 1, 0)
        grid_layout.addWidget(self.get_genericButton("Visualizza dati", self.go_dati), 1, 1)
        grid_layout.addWidget(self.get_genericButton("Gestione menu", self.go_menu), 0, 1)
        button = QPushButton("Esci")
        button.setSizePolicy(20,QSizePolicy.Expanding)
        button.clicked.connect(self.go_esci)
        grid_layout.addWidget(button, 2, 0)
        grid_layout.setRowStretch(50,50)
        self.setLayout(grid_layout)
        self.resize(400,100)
        self.setWindowTitle("Gestione amministratore")

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_dipendenti(self):
        self.vista_gestione_dipendenti = VistaGestioneDipendenti()
        self.vista_gestione_dipendenti.show()


    def go_menu(self):
        self.vista_gestione_menu = VistaGestioneMenu()
        self.vista_gestione_menu.show()

    def go_dati(self):
        self.vista_dati = VistaVisualizzaDati()
        self.vista_dati.show()

    def go_statistiche(self):
        self.vista_statistiche = VistaVisualizzaStatistiche()
        self.vista_statistiche.show()

    def go_esci(self):
        self.close()