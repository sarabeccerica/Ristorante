import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QPushButton, QSizePolicy, QGridLayout

class VistaVisualizzaDipendenti(QWidget):

    def __init__(self, parent = None):
        super(VistaVisualizzaDipendenti, self).__init__(parent)
        grid_layout = QGridLayout()
        h_layout = QVBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.list_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        h_layout.addWidget(self.list_view)
        grid_layout.addWidget(self.get_genericButton("Indietro", self.go_esci), 1, 2)
        grid_layout.setRowStretch(50,50)
        h_layout.addLayout(grid_layout)
        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Visualizza dipedenti")

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def load_dipendenti(self):
        cuochi = {}
        camerieri = {}
        if os.path.isfile('Dati\Cuochi.pickle'):
            with open('Dati\Cuochi.pickle', 'rb') as f:
                cuochi = dict(pickle.load(f))
        if os.path.isfile('Dati\Camerieri.pickle'):
            with open('Dati\Camerieri.pickle', 'rb') as f:
                camerieri = dict(pickle.load(f))
                self.dipendenti.extend(cuochi.values())
                self.dipendenti.extend(camerieri.values())

    def update_ui(self):
        self.dipendenti = []
        self.load_dipendenti()
        list_view_model = QStandardItemModel(self.list_view)
        for cuoco in self.dipendenti:
            item = QStandardItem()
            nome = f"{cuoco.nome} {cuoco.cognome} - {cuoco.codiceFiscale}"
            item.setText(nome)
            item.setEditable(False)
            list_view_model.appendRow(item)
        self.list_view.setModel(list_view_model)

    def go_esci(self):
        self.close()