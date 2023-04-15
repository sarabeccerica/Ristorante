from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from Viste.Cameriere.VistaOrdine import VistaOrdine


class VistaRicercaOrdine(QWidget):
    def __init__(self,callback):
        super(VistaRicercaOrdine, self).__init__()
        self.v_layout = QVBoxLayout()
        self.callback = callback
        self.qLines = {}
        self.add_info_text("Codice ordine","Codice ordine")
        btn_cerca = QPushButton("Cerca")
        btn_cerca.clicked.connect(self.cercaOrdine)
        self.qLines["btn_cerca"] = btn_cerca
        self.v_layout.addWidget(btn_cerca)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Ricerca ordine")

    def add_info_text(self,nome,label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def codice_prenotazione(self):
        codiceOrdine = int(self.qLines["Codice ordine"].text())
        return int(codiceOrdine)

    def cercaOrdine(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila il campo', QMessageBox.Ok, QMessageBox.Ok)
                    return
        try:
            self.vista_ordine = VistaOrdine(codice=self.codice_prenotazione())
            self.vista_ordine.show()

        except:
            QMessageBox.critical(self, 'Errore', 'Controlla di aver inserito correttamente il codice ordine'
                                 , QMessageBox.Ok, QMessageBox.Ok)
            return
        self.close()
