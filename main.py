import sys
from PyQt5.QtWidgets import QApplication

from Sistema.GestioneDati import GestioneDati
from Viste.VistaLogin import VistaLogin

if __name__ == '__main__':
    gest = GestioneDati()
    gest.backupSetup()
    app = QApplication(sys.argv)
    login = VistaLogin()
    login.show()
    sys.exit(app.exec())
