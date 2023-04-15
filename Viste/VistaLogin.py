
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel, QLineEdit, QMessageBox

from Servizio.Amministratore import Amministratore
from Servizio.Cameriere import Cameriere
from Servizio.Cuoco import Cuoco
from Viste.Amministratore.VistaGestioneAmministratore import VistaGestioneAmministratore
from Viste.Cameriere.VistaGestioneCameriere import VistaGestioneCameriere
from Viste.Cuoco.VistaGestioneCuoco import VistaGestioneCuoco


class VistaLogin(QWidget):

    def __init__(self, parent = None):
        super(VistaLogin, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("Nome Utente", "Nome Utente")
        self.add_pwd_text("Password", "Password")
        self.v_layout.addWidget(self.get_genericButton("Login",self.go_Gestione))
        self.setLayout(self.v_layout)
        self.resize(400, 90)
        self.setWindowTitle("Login")



    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def add_pwd_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        current_text.setEchoMode(QLineEdit.Password)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_Gestione(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila tutti i campi', QMessageBox.Ok,
                                         QMessageBox.Ok)
                    return
        try:
            cuoco = Cuoco()
            cameriere = Cameriere()
            amministratore = Amministratore()
            nomeUtente = self.qLines["Nome Utente"].text()
            password = self.qLines["Password"].text()

            if cameriere.verificaCredenziali(nomeUtente,password):
                self.vista_gestione_cameriere = VistaGestioneCameriere(nomeUtente)
                self.vista_gestione_cameriere.show()
            elif amministratore.verificaCredenziali(nomeUtente,password):
                self.vista_gestione_amministratore = VistaGestioneAmministratore()
                self.vista_gestione_amministratore.show()
            elif cuoco.verificaCredenziali(nomeUtente,password):
                self.vista_gestione_cuoco = VistaGestioneCuoco(nomeUtente)
                self.vista_gestione_cuoco.show()
            else:
                raise ValueError("")

        except:
            QMessageBox.critical(self, 'Errore', 'Controlla di aver inserito correttamente le credenziali'
                                 , QMessageBox.Ok, QMessageBox.Ok)
            return
