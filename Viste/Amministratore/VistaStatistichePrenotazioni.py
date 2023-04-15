import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QListView, QSizePolicy, QVBoxLayout, QPushButton


class VistaStatistichePrenotazioni(QWidget):

    def __init__(self, parent=None):
        super(VistaStatistichePrenotazioni, self).__init__(parent)
        self.list_view = QListView()
        self.list_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        h_layout = QVBoxLayout()
        h_layout.addWidget(self.list_view)
        self.load_statistiche()

        button = QPushButton("Indietro")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(self.go_indietro)
        h_layout.addWidget(button)
        self.setLayout(h_layout)
        self.resize(400, 200)
        self.setWindowTitle("Statistiche Prenotazioni")

    def load_statistiche(self):
        statistiche = {}
        if os.path.isfile('Dati\StatistichePrenotazioni.pickle'):
            with open('Dati\StatistichePrenotazioni.pickle', 'rb') as f:
                statistiche = dict(pickle.load(f))
        list_view_model = QStandardItemModel(self.list_view)
        for dato in statistiche.keys():
            item = QStandardItem()
            nome = f"{dato} : {statistiche[dato]}"
            item.setText(nome)
            item.setEditable(False)
            list_view_model.appendRow(item)
            self.list_view.setModel(list_view_model)

    def go_indietro(self):
        self.close()