from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox

from Sistema.Piatto import Piatto


class VistaAggiungiPiatto(QWidget):

    def __init__(self, callback):
        super(VistaAggiungiPiatto, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("Numero Piatto", "Numero Piatto")
        self.add_info_text("Porzioni", "Porzioni")

        btn_ok = QPushButton("Aggiungi")
        btn_ok.clicked.connect(self.aggiungiPiatto)
        self.qLines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Piatto")

    def add_info_text(self,nome,label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def aggiungiPiatto(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
                    return
        piatto = Piatto()
        try:

            numero = int(self.qLines["Numero Piatto"].text())
            porzioni = int(self.qLines["Porzioni"].text())
            if porzioni<=0:
                raise Exception("Controlla di aver inserito correttamente il numero di porzioni")
            piatto.ricercaPiatto(numero)
        except Exception as a:
            QMessageBox.critical(self, 'Errore', str(a), QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback(numero, porzioni)
        self.close()