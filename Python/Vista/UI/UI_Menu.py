from PyQt5.uic import loadUi
from PyQt5 import QtCore, Qt, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class UI_menu(QMainWindow):
    
    switch_camara = QtCore.pyqtSignal()

    
    def __init__(self, parent=None):
        super(UI_menu, self).__init__()
        loadUi('UI/templates/Menu.ui', self)
        
        #self.setWindowIcon(QIcon(ICONO))
        self.setContentsMargins(0, 0, 0, 0)
        self.label.setAttribute(Qt.WA_TranslucentBackground, True)
        # -----------------Trigger-----------------
        self.botonCamara.clicked.connect(self.switch_camara)
        
        
    def switch_camara(self):
        self.switch_camara.emit()