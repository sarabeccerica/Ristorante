from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox

from Sistema.Piatto import Piatto


class VistaAggiungiPiattoNelMenu(QWidget):

    def __init__(self, callback):
        super(VistaAggiungiPiattoNelMenu, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("Nome piatto", "Nome Piatto")
        self.add_info_text("Costo", "Costo")
        self.add_info_text("Numero piatto", "Numero piatto")
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
            nome = self.qLines["Nome piatto"].text()
            prezzo = int(self.qLines["Costo"].text())
            numeroPiatto = int(self.qLines["Numero piatto"].text())
            piatto.aggiungiPiatto(nome,prezzo,numeroPiatto)
        except Exception as a:
            QMessageBox.critical(self, 'Errore', str(a), QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()