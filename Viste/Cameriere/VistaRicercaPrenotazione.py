
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from Viste.Cameriere.VistaPrenotazione import VistaPrenotazione


class VistaRicercaPrenotazione(QWidget):
    def __init__(self,callback):
        super(VistaRicercaPrenotazione, self).__init__()
        self.v_layout = QVBoxLayout()
        self.callback = callback
        self.qLines = {}
        self.add_info_text("Nome prenotazione","Nome prenotazione")
        btn_cerca = QPushButton("Cerca")
        btn_cerca.clicked.connect(self.cercaPrenotazione)
        self.qLines["btn_cerca"] = btn_cerca
        self.v_layout.addWidget(btn_cerca)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Ricerca prenotazione")

    def add_info_text(self,nome,label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def numero_prenotazione(self):
        nomeP = str(self.qLines["Nome prenotazione"].text())
        return str(nomeP)

    def cercaPrenotazione(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila il campo', QMessageBox.Ok, QMessageBox.Ok)
                    return
        try:
            self.vista_prenotazione = VistaPrenotazione(nome=self.numero_prenotazione(),callback = self.callback)
            self.vista_prenotazione.show()

        except:
            QMessageBox.critical(self, 'Errore', 'Controlla di aver inserito correttamente il numero della prenotazione'
                                 , QMessageBox.Ok, QMessageBox.Ok)
            return
        self.close()