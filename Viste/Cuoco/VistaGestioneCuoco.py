from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from Viste.Cuoco.VistaModificaCuoco import VistaModificaCuoco
from Viste.Cuoco.VistaVisualizzaMessaggiCuoco import VistaVisualizzaMessaggiCuoco


class VistaGestioneCuoco(QWidget):

    def __init__(self,nomeCuoco):
        super(VistaGestioneCuoco,self).__init__()
        self.nomeCuoco = nomeCuoco
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_genericButton("Gestione account", self.go_account), 0, 0)
        grid_layout.addWidget(self.get_genericButton("Gestione messaggi", self.go_messaggi), 1, 0)
        button = QPushButton("Esci")
        button.setSizePolicy(20,QSizePolicy.Expanding)
        button.clicked.connect(self.go_esci)
        grid_layout.addWidget(button, 2, 0)
        grid_layout.setRowStretch(50,50)
        self.setLayout(grid_layout)
        self.resize(400,100)
        self.setWindowTitle("Gestione cuoco")

    def get_genericButton(self,titolo,on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_account(self):
        self.vista_modifica_cuoco = VistaModificaCuoco(self.nomeCuoco)
        self.vista_modifica_cuoco.show()

    def go_messaggi(self):
        self.vista_visualizza_messaggi = VistaVisualizzaMessaggiCuoco(nomeCuoco = self.nomeCuoco)
        self.vista_visualizza_messaggi.show()

    def go_esci(self):
        self.close()