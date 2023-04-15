import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QListView, QSizePolicy, QVBoxLayout, QPushButton


class VistaVisualizzaScontrini(QWidget):

    def __init__(self, parent=None):
        super(VistaVisualizzaScontrini, self).__init__(parent)
        self.list_view = QListView()
        self.list_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        h_layout = QVBoxLayout()
        h_layout.addWidget(self.list_view)
        self.load_scontrini()

        button = QPushButton("Indietro")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(self.go_indietro)
        h_layout.addWidget(button)
        self.setLayout(h_layout)
        self.resize(400, 200)
        self.setWindowTitle("Visualizza Scontrini")

    def load_scontrini(self):
        scontrini = {}
        if os.path.isfile('Dati\Scontrini.pickle'):
            with open('Dati\Scontrini.pickle', 'rb') as f:
                scontrini = dict(pickle.load(f))
        list_view_model = QStandardItemModel(self.list_view)
        for scontrino in scontrini.values():
            item = QStandardItem()
            nome = f"{scontrino.codice} {scontrino.dataOra} - {scontrino.numeroTavolo}  \n{scontrino.stampaPiatti()} {scontrino.totale}\n"
            item.setText(nome)
            item.setEditable(False)
            list_view_model.appendRow(item)
            self.list_view.setModel(list_view_model)

    def go_indietro(self):
        self.close()