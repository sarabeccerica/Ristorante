from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox

from Gestione.Prenotazione import Prenotazione


class VistaAssegnaConPrenotazione(QWidget):

    def __init__(self,parent = None):
        super(VistaAssegnaConPrenotazione, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("Nome prenotazione", "Nome prenotazione")

        btn_ok = QPushButton("Assegna")
        btn_ok.clicked.connect(self.assegnaTavoli)
        self.qLines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Arrivo prenotati")

    def add_info_text(self,nome,label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def assegnaTavoli(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
                    return

        try:
            prenotazione = Prenotazione()
            nomePrenotazione = self.qLines["Nome prenotazione"].text()
            vettTavoli = prenotazione.arrivoPrenotati(nomePrenotazione)
            listaTavoli = ""
            for tavolo in vettTavoli:
                listaTavoli+= str(tavolo)
            successo = QMessageBox()
            successo.setText(listaTavoli)
            successo.exec()
        except:
            QMessageBox.critical(self, 'Errore', 'Prenotazione non trovata'
                                 , QMessageBox.Ok, QMessageBox.Ok)
            return
        self.close()