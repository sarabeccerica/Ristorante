from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from Viste.Amministratore.VistaGestioneAccountCameriere import VistaGestioneAccountCameriere

class VistaRicercCameriere(QWidget):
    def __init__(self,parent = None):
        super(VistaRicercCameriere, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("Codice fiscale","Codice fiscale")
        btn_cerca = QPushButton("Cerca")
        btn_cerca.clicked.connect(self.cercaCameriere)
        self.qLines["btn_cerca"] = btn_cerca
        self.v_layout.addWidget(btn_cerca)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Ricerca cameriere")

    def add_info_text(self,nome,label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def codice_fiscale(self):
        codiceFiscale = str(self.qLines["Codice fiscale"].text())
        return str(codiceFiscale)

    def cercaCameriere(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila il campo', QMessageBox.Ok, QMessageBox.Ok)
                    return
        try:
            self.vista_gestione_cameriere = VistaGestioneAccountCameriere(cf=self.codice_fiscale())
            self.vista_gestione_cameriere.show()
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla di aver inserito correttamente il codice fiscale'
                                 , QMessageBox.Ok, QMessageBox.Ok)
            return
        self.close()