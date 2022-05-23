from PyQt5.uic import loadUi
from PyQt5 import QtCore, Qt, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from Constantes import *

class UI_menu(QMainWindow):
    
    switch_camara = QtCore.pyqtSignal()

    
    def __init__(self, parent=None):
        super(UI_menu, self).__init__()
        loadUi('UI/templates/Menu.ui', self)
        
        #self.setWindowIcon(QIcon(ICONO))
        self.setContentsMargins(0, 0, 0, 0)
        self.label.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ImagenLabel.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ImagenLabel.setPixmap(QtGui.QPixmap('Utiles/Protanopia.png'))      
        # -----------------Trigger-----------------
        self.botonCamara.clicked.connect(self.abrirCamara)
        
        
    def abrirCamara(self):
        self.switch_camara.emit()