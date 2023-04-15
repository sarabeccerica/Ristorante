from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from Viste.Cameriere.VistaScontrino import VistaScontrino


class VistaStampaScontrino(QWidget):
    def __init__(self,callback):
        super(VistaStampaScontrino, self).__init__()
        self.v_layout = QVBoxLayout()
        self.callback = callback
        self.qLines = {}
        self.add_info_text("Numero tavolo","Numero tavolo")
        btn_stampa = QPushButton("Stampa")
        btn_stampa.clicked.connect(self.stampaScontrino)
        self.qLines["btn_stampa"] = btn_stampa
        self.v_layout.addWidget(btn_stampa)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Stampa scontrino")

    def add_info_text(self,nome,label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def numero_tavolo(self):
        numeroTavolo = int(self.qLines["Numero tavolo"].text())
        return int(numeroTavolo)

    def stampaScontrino(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila il campo', QMessageBox.Ok, QMessageBox.Ok)
                    return
        try:
            self.vista_scontrinio = VistaScontrino(num=self.numero_tavolo(),callback = self.callback)
            self.vista_scontrinio.show()
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla di aver inserito correttamente il numero del tavolo', QMessageBox.Ok, QMessageBox.Ok)
            return
        self.close()

