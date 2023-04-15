import os
import pickle
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QPushButton, QSizePolicy, QGridLayout

from Viste.Cameriere.VistaRicercaScontrino import VistaRicercaScontrino
from Viste.Cameriere.VistaStampaScontrino import VistaStampaScontrino


class VistaGestioneScontrini(QWidget):

    def __init__(self, parent = None):
        super(VistaGestioneScontrini, self).__init__(parent)
        grid_layout = QGridLayout()
        h_layout = QVBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.list_view.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        h_layout.addWidget(self.list_view)
        grid_layout.addWidget(self.get_genericButton("Stampa scontrino", self.go_stampaScontrino), 1, 1)
        grid_layout.addWidget(self.get_genericButton("Cerca scontrino",self.go_cercaScontrino),1,2)
        grid_layout.addWidget(self.get_genericButton("Indietro", self.go_GestioneCameriere), 1, 0)
        grid_layout.setRowStretch(50,50)
        h_layout.addLayout(grid_layout)
        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Gestione scontrini")

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def load_scontrini(self):
        scontrini = {}
        if os.path.isfile('Dati\Scontrini.pickle'):
            with open('Dati\Scontrini.pickle', 'rb') as f:
                scontrini = dict(pickle.load(f))
                self.scontrini.extend(scontrini.values())


    def update_ui(self):
        self.scontrini = []
        self.load_scontrini()
        list_view_model = QStandardItemModel(self.list_view)
        for scontrino in self.scontrini:
            item = QStandardItem()
            nome = f"{scontrino.codice} {scontrino.dataOra} - {scontrino.numeroTavolo} \n {scontrino.stampaPiatti()} " \
                   f"{scontrino.totale}"
            item.setText(nome)
            item.setEditable(False)
            list_view_model.appendRow(item)
        self.list_view.setModel(list_view_model)

    def go_stampaScontrino(self):
        self.vista_stampa_scontrino = VistaStampaScontrino(callback=self.update_ui)
        self.vista_stampa_scontrino.show()

    def go_cercaScontrino(self):
        self.vista_ricerca_ordine = VistaRicercaScontrino(callback = self.update_ui)
        self.vista_ricerca_ordine.show()

    def go_GestioneCameriere(self):
        self.close()