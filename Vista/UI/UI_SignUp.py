from PyQt5.uic import loadUi
from PyQt5 import QtCore, Qt, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from Constantes import *

class UI_SignUp(QMainWindow):
    
    switch_Login = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super(UI_SignUp, self).__init__()
        loadUi('UI/templates/SignUp.ui', self)
        
        #self.setWindowIcon(QIcon(ICONO))
        self.setContentsMargins(0, 0, 0, 0)
        self.label.setAttribute(Qt.WA_TranslucentBackground, True)
        self.label_2.setAttribute(Qt.WA_TranslucentBackground, True)
        # -----------------Trigger-----------------
        self.botonRegistro.clicked.connect(self.abrirLogin)
    
    def abrirLogin(self):
        self.switch_Login.emit()
        
 
        