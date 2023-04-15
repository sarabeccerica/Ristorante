from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout, QVBoxLayout, QSizePolicy, QLabel, QLineEdit, QMessageBox, \
    QListView

from Gestione.Ordine import Ordine
from Servizio.Cameriere import Cameriere
from Viste.Cameriere.VistaAggiungiPiatto import VistaAggiungiPiatto


class VistaAggiungiOrdine(QWidget):

    def __init__(self,callback):
        super(VistaAggiungiOrdine, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("Numero Tavolo","Numero Tavolo")
        grid = QGridLayout()
        self.listaPiatti = dict()
        self.list_view = QListView()
        self.list_view.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.v_layout.addWidget(self.list_view)
        grid.addWidget(self.get_genericButton("Aggiungi Piatto", self.go_aggiungiPiatto), 0, 0)
        grid.addWidget(self.get_genericButton("Conferma", self.go_Conferma), 0, 1)
        grid.addWidget(self.get_genericButton("Indietro", self.go_Indietro), 0, 2)

        grid.setRowStretch(50, 50)
        self.v_layout.addLayout(grid)
        self.setLayout(self.v_layout)
        self.resize(600, 300)
        self.setWindowTitle("Aggiungi Ordine")

    def add_info_text(self,nome,label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_aggiungiPiatto(self):
        self.vista_aggiungi_piatto = VistaAggiungiPiatto(callback=self.piattoAggiunto)
        self.vista_aggiungi_piatto.show()

    def go_Indietro(self):
        self.close()

    def piattoAggiunto(self, piatto,quantita):
        self.listaPiatti[piatto] = quantita
        list_view_model = QStandardItemModel(self.list_view)
        for piatto in self.listaPiatti.keys():
            item = QStandardItem()
            nome = f"Numero piatto: {piatto} Quantità: {self.listaPiatti[piatto]}"
            item.setText(nome)
            item.setEditable(False)
            list_view_model.appendRow(item)
        self.list_view.setModel(list_view_model)


    def go_Conferma(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
                    return
        ordine = Ordine()
        try:
            cam = Cameriere()
            numeroTavolo = int(self.qLines["Numero Tavolo"].text())
            ordine.aggiungiOrdine(numeroTavolo,self.listaPiatti)
            cam.notificaDipendente(ordine)
        except Exception as a:
            QMessageBox.critical(self, 'Errore', str(a), QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()