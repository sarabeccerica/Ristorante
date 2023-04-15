from datetime import datetime

from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QVBoxLayout, QMessageBox, QPushButton, QGridLayout

from Gestione.Prenotazione import Prenotazione

class VistaModificaPrenotazione(QWidget):

    def __init__(self, nomeP,callback):
        super(VistaModificaPrenotazione,self).__init__()
        self.callback = callback
        self.nomeP = str(nomeP)
        prenotazione = Prenotazione()
        self.qLines = {}
        self.prenotazione = prenotazione.ricercaPrenotazione(self.nomeP)
        self.v_layout = QVBoxLayout()

        self.grid = QGridLayout()
        self.v_layout.addWidget(QLabel("Nome    "+ self.nomeP))
        self.add_info_text("Data", "Data",str(self.prenotazione.dataOra.day) +'/'+ str(self.prenotazione.dataOra.month)
                           +'/'+ str(self.prenotazione.dataOra.year) + ' ' + str(self.prenotazione.dataOra.hour) + ':' +
                           str(self.prenotazione.dataOra.minute))
        self.add_info_text("Numero persone", "Numero persone",str(self.prenotazione.numeroPersone))

        btn_ok = QPushButton("Modifica")
        btn_ok.clicked.connect(self.go_modifica)
        self.qLines["btn_ok"] = btn_ok
        self.grid.addWidget(btn_ok,1,1)

        btn_indietro = QPushButton("Indietro")
        btn_indietro.clicked.connect(self.go_indietro)
        self.qLines["btn_indietro"] = btn_indietro
        self.grid.addWidget(btn_indietro,1,0)
        self.v_layout.addLayout(self.grid)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica Account")


    def add_info_text(self,nome,label,stringa):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        current_text.setText(stringa)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def go_modifica(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
                    return
        try:
            prenotazione = Prenotazione()
            dataOra = datetime.strptime(self.qLines["Data"].text(), '%d/%m/%Y %H:%M')
            numeroPersone = int(self.qLines["Numero persone"].text())
            prenotazione.modificaPrenotazione(dataOra,self.nomeP,numeroPersone)
        except Exception as a:
            QMessageBox.critical(self, 'Errore', str(a), QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()

    def go_indietro(self):
        self.close()