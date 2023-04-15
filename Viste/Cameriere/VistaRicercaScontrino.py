from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from Viste.Cameriere.VistaScontrinoCercato import VistaScontrinoCercato


class VistaRicercaScontrino(QWidget):
    def __init__(self,callback):
        super(VistaRicercaScontrino, self).__init__()
        self.v_layout = QVBoxLayout()
        self.callback = callback
        self.qLines = {}
        self.add_info_text("Codice scontrino","Codice scontrino")
        btn_cerca = QPushButton("Cerca")
        btn_cerca.clicked.connect(self.cercaScontrino)
        self.qLines["btn_cerca"] = btn_cerca
        self.v_layout.addWidget(btn_cerca)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Ricerca scontrino")

    def add_info_text(self,nome,label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def codice_scontrino(self):
        codiceScontrino = int(self.qLines["Codice scontrino"].text())
        return int(codiceScontrino)

    def cercaScontrino(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila il campo', QMessageBox.Ok, QMessageBox.Ok)
                    return
        try:
            self.vista_scontrino = VistaScontrinoCercato(codice=self.codice_scontrino(),callback=self.callback)
            self.vista_scontrino.show()

        except:
            QMessageBox.critical(self, 'Errore', 'Controlla di aver inserito correttamente il codice dello scontrino'
                                 , QMessageBox.Ok, QMessageBox.Ok)
            return
        self.close()