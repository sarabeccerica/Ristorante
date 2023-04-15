from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox

from Gestione.Prenotazione import Prenotazione
from Gestione.Tavolo import Tavolo


class VistaAssegnaSenzaPrenotazione(QWidget):

    def __init__(self, parent=None):
        super(VistaAssegnaSenzaPrenotazione, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("Tavoli necessari", "Tavoli necessari")

        btn_ok = QPushButton("Assegna")
        btn_ok.clicked.connect(self.assegnaTavoli)
        self.qLines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Arrivo clienti")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def assegnaTavoli(self):
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Perfavore compila tutti i campi', QMessageBox.Ok,
                                         QMessageBox.Ok)
                    return

        try:
            tavolo = Tavolo()
            tavoliNecessari = int(self.qLines["Tavoli necessari"].text())
            vettTavoli = tavolo.assegnaTavoloSenzaPrenotazione(tavoliNecessari)
            listaTavoli = ""
            for tavolo in vettTavoli.values():
                listaTavoli += tavolo.__str__()
            successo = QMessageBox()
            successo.setText(listaTavoli)
            successo.exec()
        except Exception as err:
            QMessageBox.critical(self, 'Errore', str(err)
                                 , QMessageBox.Ok, QMessageBox.Ok)
            return
        self.close()