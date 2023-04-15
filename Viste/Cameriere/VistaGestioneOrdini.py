import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QPushButton, QSizePolicy, QGridLayout

from Viste.Cameriere.VistaAggiungiOrdine import VistaAggiungiOrdine
from Viste.Cameriere.VistaRicercaOrdine import VistaRicercaOrdine


class VistaGestioneOrdini(QWidget):

    def __init__(self, parent = None):
        super(VistaGestioneOrdini, self).__init__(parent)
        grid_layout = QGridLayout()
        h_layout = QVBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.list_view.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        h_layout.addWidget(self.list_view)
        grid_layout.addWidget(self.get_genericButton("Aggiungi ordine", self.go_aggiungiOrdine), 1, 1)
        grid_layout.addWidget(self.get_genericButton("Cerca ordine",self.go_cercaOrdine),1,2)
        grid_layout.addWidget(self.get_genericButton("Indietro", self.go_GestioneCameriere), 1, 0)
        grid_layout.setRowStretch(50,50)
        h_layout.addLayout(grid_layout)
        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Gestione ordini")

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def load_ordini(self):
        if os.path.isfile('Dati\Ordini.pickle'):
            with open('Dati\Ordini.pickle', 'rb') as f:
                ordini = dict(pickle.load(f))
                self.ordini.extend(ordini.values())


    def update_ui(self):
        self.ordini = []
        self.load_ordini()
        list_view_model = QStandardItemModel(self.list_view)
        for ordine in self.ordini:
            item = QStandardItem()
            nome = f"{ordine.codice} {ordine.statoOrdine} - {ordine.stampaListaPiatti()}"
            item.setText(nome)
            item.setEditable(False)
            list_view_model.appendRow(item)
        self.list_view.setModel(list_view_model)

    def go_aggiungiOrdine(self):
        self.vista_aggiungi_ordine = VistaAggiungiOrdine(callback=self.update_ui)
        self.vista_aggiungi_ordine.show()

    def go_cercaOrdine(self):
        self.vista_ricerca_ordine = VistaRicercaOrdine(callback = self.update_ui)
        self.vista_ricerca_ordine.show()

    def go_GestioneCameriere(self):
        self.close()