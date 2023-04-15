from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from Viste.Cameriere.VistaAssegnaTavoli import VistaAssegnaTavoli
from Viste.Cameriere.VistaGestioneOrdini import VistaGestioneOrdini
from Viste.Cameriere.VistaGestionePrenotazione import VistaGestionePrenotazione
from Viste.Cameriere.VistaGestioneScontrini import VistaGestioneScontrini
from Viste.Cameriere.VistaModificaCameriere import VistaModificaCameriere
from Viste.Cameriere.VistaVisualizzaMessaggiCameriere import VistaVisualizzaMessaggiCameriere


class VistaGestioneCameriere(QWidget):

    def __init__(self,nomeCameriere):
        super(VistaGestioneCameriere,self).__init__()
        self.nomeCameriere = nomeCameriere
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_genericButton("Gestione account", self.go_account), 1, 0)
        grid_layout.addWidget(self.get_genericButton("Assegna tavoli", self.go_tavoli), 1, 1)
        grid_layout.addWidget(self.get_genericButton("Gestione messaggi", self.go_messaggi), 1, 2)
        grid_layout.addWidget(self.get_genericButton("Gestione prenotazioni", self.go_prenotazioni), 0, 0)
        grid_layout.addWidget(self.get_genericButton("Gestione ordini", self.go_ordini), 0,2)
        grid_layout.addWidget(self.get_genericButton("Gestione scontrini", self.go_scontrino), 0, 1)
        button = QPushButton("Esci")
        button.setSizePolicy(20,QSizePolicy.Expanding)
        button.clicked.connect(self.go_esci)
        grid_layout.addWidget(button, 2, 0)
        grid_layout.setRowStretch(50,50)
        self.setLayout(grid_layout)
        self.resize(400,100)
        self.setWindowTitle("Gestione cameriere")

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_account(self):
        self.vista_modifica_cameriere = VistaModificaCameriere(self.nomeCameriere)
        self.vista_modifica_cameriere.show()

    def go_scontrino(self):
        self.vista_stampa_scontrino = VistaGestioneScontrini()
        self.vista_stampa_scontrino.show()

    def go_ordini(self):
        self.vista_gestione_ordini = VistaGestioneOrdini()
        self.vista_gestione_ordini.show()

    def go_prenotazioni(self):
        self.vista_gestione_prenotazione = VistaGestionePrenotazione()
        self.vista_gestione_prenotazione.show()


    def go_messaggi(self):
        self.vista_visualizza_messaggi = VistaVisualizzaMessaggiCameriere(nomeCameriere = self.nomeCameriere)
        self.vista_visualizza_messaggi.show()

    def go_tavoli(self):
        self.vista_assegna_tavoli = VistaAssegnaTavoli()
        self.vista_assegna_tavoli.show()

    def go_esci(self):
        self.close()