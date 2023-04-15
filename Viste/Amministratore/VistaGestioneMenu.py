import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QPushButton, QSizePolicy, QGridLayout

from Viste.Amministratore.VistaAggiungiPiattoNelMenu import VistaAggiungiPiattoNelMenu
from Viste.Amministratore.VistaRicercaPiatto import VistaRicercaPiatto


class VistaGestioneMenu(QWidget):

    def __init__(self, parent = None):
        super(VistaGestioneMenu, self).__init__(parent)
        grid_layout = QGridLayout()
        h_layout = QVBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.list_view.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        h_layout.addWidget(self.list_view)
        grid_layout.addWidget(self.get_genericButton("Aggiungi piatto", self.go_aggiungiPiatto), 1, 0)
        grid_layout.addWidget(self.get_genericButton("cerca piatto", self.go_cercaPiatto), 1, 1)
        grid_layout.addWidget(self.get_genericButton("Indietro", self.go_GestioneAmministratore), 1, 2)
        grid_layout.setRowStretch(50,50)
        h_layout.addLayout(grid_layout)
        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Gestione menu")

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def load_piatti(self):
        if os.path.isfile('Dati\Piatti.pickle'):
            with open('Dati\Piatti.pickle', 'rb') as f:
                piatti = dict(pickle.load(f))
                self.piatti.extend(piatti.values())


    def update_ui(self):
        self.piatti = []
        self.load_piatti()
        list_view_model = QStandardItemModel(self.list_view)
        for piatto in self.piatti:
            item = QStandardItem()
            nome = f"{piatto.numero} {piatto.nome} - {piatto.prezzo}€"
            item.setText(nome)
            item.setEditable(False)
            list_view_model.appendRow(item)
        self.list_view.setModel(list_view_model)

    def go_aggiungiPiatto(self):
        self.vista_aggiungi_piatto = VistaAggiungiPiattoNelMenu(callback = self.update_ui)
        self.vista_aggiungi_piatto.show()

    def go_cercaPiatto(self):
        self.vista_cerc_piatto = VistaRicercaPiatto(callback=self.update_ui)
        self.vista_cerc_piatto.show()

    def go_GestioneAmministratore(self):
        self.close()