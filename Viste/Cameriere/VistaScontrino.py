
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout

from Gestione.Scontrino import Scontrino

class VistaScontrino(QWidget):
    def __init__(self,num,callback):
        super(VistaScontrino, self).__init__()
        self.num = num
        self.callback = callback
        scontrino = Scontrino()
        scontrino.aggiungiScontrino(int(self.num))
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(QLabel("Codice"),0,0)
        self.grid_layout.addWidget(QLabel(str(scontrino.codice)),0,1)
        self.grid_layout.addWidget(QLabel("Tavolo: "),1,0)
        self.grid_layout.addWidget(QLabel(str(scontrino.numeroTavolo)),1,1)
        self.grid_layout.addWidget(QLabel("Data: "),2,0)
        self.grid_layout.addWidget(QLabel(str(scontrino.dataOra)),2,1)
        self.grid_layout.addWidget(QLabel("Piatti: "),3,0)
        self.grid_layout.addWidget(QLabel(scontrino.stampaPiatti()),3,1)
        self.grid_layout.addWidget(QLabel("Totale: "),4,0)
        self.grid_layout.addWidget(QLabel(str(scontrino.totale)),4,1)

        btn_indietro = QPushButton("Indietro")
        btn_indietro.clicked.connect(self.indietro)
        self.grid_layout.addWidget(btn_indietro)
        self.setLayout(self.grid_layout)
        self.setWindowTitle("Scontrino")

    def indietro(self):
        self.close()
        self.callback()

