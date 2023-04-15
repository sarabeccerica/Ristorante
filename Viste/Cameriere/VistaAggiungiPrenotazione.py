from datetime import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from Gestione.Prenotazione import Prenotazione


class VistaAggiungiPrenotazione(QWidget):
    def __init__(self,callback):
        super(VistaAggiungiPrenotazione, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("Data","Data")
        self.add_info_text("Nome", "Nome")
        self.add_info_text("Numero Persone","Numero Persone")

        btn_ok = QPushButton("Aggiungi")
        btn_ok.clicked.connect(self.aggiungiPrenotazione)
        self.qLines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuova prenotazione")

    def add_info_text(self,nome,label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def aggiungiPrenotazione(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
                    return
        try:
            prenotazione = Prenotazione()
            data = datetime.strptime(self.qLines["Data"].text(), '%d/%m/%Y %H:%M')
            nome = self.qLines["Nome"].text()
            numeroPersone = int(self.qLines["Numero Persone"].text())
            prenotazione.aggiungiPrenotazione(data,nome,numeroPersone)

        except Exception as a:
            QMessageBox.critical(self, 'Errore', str(a), QMessageBox.Ok, QMessageBox.Ok)
            return
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla di aver inserito correttamente le credenziali'
                                 , QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()