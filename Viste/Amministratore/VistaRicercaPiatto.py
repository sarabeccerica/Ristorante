from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from Viste.Amministratore.VistaEliminaPiatto import VistaEliminaPiatto


class VistaRicercaPiatto(QWidget):
    def __init__(self,callback):
        super(VistaRicercaPiatto, self).__init__()
        self.callback=callback
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("Numero Piatto","Numero Piatto")
        btn_cerca = QPushButton("Cerca")
        btn_cerca.clicked.connect(self.cercaPiatto)
        self.qLines["btn_cerca"] = btn_cerca
        self.v_layout.addWidget(btn_cerca)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Ricerca Piatto")

    def add_info_text(self,nome,label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def numero_piatto(self):
        numeroPiatto = int(self.qLines["Numero Piatto"].text())
        return int(numeroPiatto)

    def cercaPiatto(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila il campo', QMessageBox.Ok, QMessageBox.Ok)
                    return
        try:
            self.vista_elimina_piatto = VistaEliminaPiatto(callback = self.callback,numeroPiatto = self.numero_piatto())
            self.vista_elimina_piatto.show()
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla di aver inserito correttamente il numero del piatto'
                                 , QMessageBox.Ok, QMessageBox.Ok)
            return
        self.close()