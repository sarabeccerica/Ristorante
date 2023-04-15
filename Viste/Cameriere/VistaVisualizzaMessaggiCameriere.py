
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QPushButton, QSizePolicy, QGridLayout

from Servizio.Cameriere import Cameriere
from Viste.Cameriere.VistaCercaMessaggiCameriere import VistaCercaMessaggiCameriere


class VistaVisualizzaMessaggiCameriere(QWidget):

    def __init__(self,nomeCameriere):
        super(VistaVisualizzaMessaggiCameriere, self).__init__()
        grid_layout = QGridLayout()
        h_layout = QVBoxLayout()
        self.nomeCameriere = nomeCameriere
        self.cameriere = Cameriere()
        self.list_view = QListView()
        self.update_ui()
        self.list_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        h_layout.addWidget(self.list_view)

        grid_layout.addWidget(self.get_genericButton("Consegnato", self.go_cercaMessaggio), 1, 1)
        grid_layout.addWidget(self.get_genericButton("Indietro", self.go_esci), 1, 2)
        grid_layout.setRowStretch(50,50)
        h_layout.addLayout(grid_layout)
        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Visualizza messaggi")

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def load_messaggi(self):
        messaggi = self.cameriere.visualizzaListaMessaggi()
        self.messaggi = messaggi

    def update_ui(self):
        self.messaggi = dict()
        self.load_messaggi()
        list_view_model = QStandardItemModel(self.list_view)
        for messaggio in self.messaggi.keys():
            item = QStandardItem()
            nome = f"{messaggio} {self.messaggi[messaggio]}"
            item.setText(nome)
            item.setEditable(False)
            list_view_model.appendRow(item)
        self.list_view.setModel(list_view_model)

    def go_cercaMessaggio(self):
        self.vista_cerca_messaggi = VistaCercaMessaggiCameriere(callback = self.update_ui)
        self.vista_cerca_messaggi.show()

    def go_esci(self):
        self.close()