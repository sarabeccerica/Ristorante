from datetime import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from Servizio.Cuoco import Cuoco


class VistaAggiungiCuoco(QWidget):
    def __init__(self,parent = None):
        super(VistaAggiungiCuoco, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("Nome","Nome")
        self.add_info_text("Cognome","Cognome")
        self.add_info_text("Data di nascita", "Data di nascita")
        self.add_info_text("Codice fiscale", "Codice fiscale")
        self.add_info_text("Indirizzo e-mail", "Indirizzo e-mail")
        self.add_info_text("Telefono","Telefono")
        self.add_info_text("Password","Password")

        btn_ok = QPushButton("Aggiungi")
        btn_ok.clicked.connect(self.aggiungiCuoco)
        self.qLines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Account")

    def add_info_text(self,nome,label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def aggiungiCuoco(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
                    return
        cuoco = Cuoco()
        try:
            nome = self.qLines["Nome"].text()
            cognome = self.qLines["Cognome"].text()
            dataNscita = datetime.strptime(self.qLines["Data di nascita"].text(), '%d/%m/%Y')
            codiceFiscale = self.qLines["Codice fiscale"].text()
            indirizzoEmail = self.qLines["Indirizzo e-mail"].text()
            telefono = self.qLines["Telefono"].text()
            password = self.qLines["Password"].text()
            cuoco.aggiungiCuoco(nome,cognome,dataNscita,codiceFiscale,indirizzoEmail,password,telefono)
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla di aver inserito correttamente la data di nascita'
                                 , QMessageBox.Ok, QMessageBox.Ok)
            return
        self.close()
