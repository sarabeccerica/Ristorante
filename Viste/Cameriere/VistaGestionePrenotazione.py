import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QPushButton, QSizePolicy, QGridLayout

from Viste.Cameriere.VistaAggiungiPrenotazione import VistaAggiungiPrenotazione
from Viste.Cameriere.VistaRicercaPrenotazione import VistaRicercaPrenotazione


class VistaGestionePrenotazione(QWidget):

    def __init__(self, parent = None):
        super(VistaGestionePrenotazione, self).__init__(parent)
        grid_layout = QGridLayout()
        h_layout = QVBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.list_view.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        h_layout.addWidget(self.list_view)
        grid_layout.addWidget(self.get_genericButton("Aggiungi prenotazione", self.go_aggiungiPrenotazione), 1, 1)
        grid_layout.addWidget(self.get_genericButton("Cerca prenotazione",self.go_cercaPrenotazione),1,2)
        grid_layout.addWidget(self.get_genericButton("Indietro", self.go_GestioneCameriere),1,0)
        grid_layout.setRowStretch(50,50)
        h_layout.addLayout(grid_layout)
        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Gestione prenotazioni")

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def load_prenotazioni(self):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
                self.prenotazioni.extend(prenotazioni.values())


    def update_ui(self):
        self.prenotazioni = []
        self.load_prenotazioni()
        list_view_model = QStandardItemModel(self.list_view)
        for prenotazione in self.prenotazioni:
            item = QStandardItem()
            nome = f"{prenotazione.nome} {prenotazione.numeroPersone} - {prenotazione.dataOra}"
            item.setText(nome)
            item.setEditable(False)
            list_view_model.appendRow(item)
        self.list_view.setModel(list_view_model)

    def go_aggiungiPrenotazione(self):
        self.vista_aggiungi_prenotazione = VistaAggiungiPrenotazione(callback=self.update_ui)
        self.vista_aggiungi_prenotazione.show()

    def go_cercaPrenotazione(self):
        self.vista_ricerca_prenotazione = VistaRicercaPrenotazione(callback=self.update_ui)
        self.vista_ricerca_prenotazione.show()

    def go_GestioneCameriere(self):
        self.close()