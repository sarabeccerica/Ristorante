
from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QVBoxLayout, QMessageBox, QPushButton, QGridLayout

from Sistema.Piatto import Piatto


class VistaModificaPiatto(QWidget):

    def __init__(self, numero,callback):
        super(VistaModificaPiatto,self).__init__()
        self.callback = callback
        self.numeroPiatto = numero
        piatto = Piatto()
        self.qLines = {}
        self.piatto = piatto.ricercaPiatto(numero)
        self.v_layout = QVBoxLayout()

        self.v_layout.addWidget(QLabel("Numero    "+ str(self.numeroPiatto)))
        self.add_info_text("Nome", "Nome",self.piatto.nome)
        self.add_info_text("Prezzo", "Prezzo",str(self.piatto.prezzo))

        self.grid = QGridLayout()
        btn_ok = QPushButton("Modifica")
        btn_ok.clicked.connect(self.go_modifica)
        self.qLines["btn_ok"] = btn_ok
        self.grid.addWidget(btn_ok,0,0)

        btn_indietro = QPushButton("Indietro")
        btn_indietro.clicked.connect(self.go_indietro)
        self.qLines["btn_indietro"] = btn_indietro
        self.grid.addWidget(btn_indietro,0,1)
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
        piatto = Piatto()
        try:
            nome = self.qLines["Nome"].text()
            prezzo = int(self.qLines["Prezzo"].text())
            piatto.modificaPiatto(nome, prezzo,self.numeroPiatto)
        except Exception as a:
            QMessageBox.critical(self, 'Errore', str(a), QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()

    def go_indietro(self):
        self.close()