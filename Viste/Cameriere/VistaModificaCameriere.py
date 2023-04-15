from datetime import datetime

from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QVBoxLayout, QMessageBox, QPushButton, QGridLayout

from Servizio.Cameriere import Cameriere


class VistaModificaCameriere(QWidget):

    def __init__(self, nomeAccount):
        super(VistaModificaCameriere,self).__init__()
        self.nomeAccount = str(nomeAccount)
        cameriere = Cameriere()
        self.qLines = {}
        self.cameriere = cameriere.ricercaDipendente(self.nomeAccount)
        self.v_layout = QVBoxLayout()
        self.add_info_text("Nome", "Nome",self.cameriere.nome)
        self.add_info_text("Cognome", "Cognome",self.cameriere.cognome)
        self.add_info_text("Data di Nascita", "Data di Nascita",str(self.cameriere.dataNascita.day) +'/'+ str(self.cameriere.dataNascita.month) +'/'+ str(self.cameriere.dataNascita.year))
        self.add_info_text("Codice Fiscale", "Codice Fiscale",self.cameriere.codiceFiscale)
        self.add_info_text("Indirizzo E-mail", "Indirizzo E-mail",self.cameriere.email)
        self.add_info_text("Password", "Password",self.cameriere.password)
        self.add_info_text("Telefono", "Telefono",self.cameriere.telefono)

        self.grid = QGridLayout()
        btn_ok = QPushButton("Modifica")
        btn_ok.clicked.connect(self.go_modifica)
        self.qLines["btn_ok"] = btn_ok
        self.grid.addWidget(btn_ok,1,1)

        btn_indietro = QPushButton("Indietro")
        btn_indietro.clicked.connect(self.go_modifica)
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
            cameriere = Cameriere()
            nome = self.qLines["Nome"].text()
            cognome = self.qLines["Cognome"].text()
            dataNascita = datetime.strptime(self.qLines["Data di Nascita"].text(), '%d/%m/%Y')
            codiceFiscale = self.qLines["Codice Fiscale"].text()
            indirizzoEmail = self.qLines["Indirizzo E-mail"].text()
            telefono = self.qLines["Telefono"].text()
            password = self.qLines["Password"].text()
            cameriere.modificaCameriere(nome, cognome, dataNascita, codiceFiscale, indirizzoEmail, password, telefono)
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla di aver inserito correttamente la data di nascita', QMessageBox.Ok, QMessageBox.Ok)
            return
        self.close()