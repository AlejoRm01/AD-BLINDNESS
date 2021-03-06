from PyQt5.uic import loadUi
from PyQt5 import QtCore, Qt, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from Constantes import *

class UI_SignUp(QMainWindow):
    
    switch_Login = QtCore.pyqtSignal()
    sigValidar = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super(UI_SignUp, self).__init__()
        loadUi('UI/templates/SignUp.ui', self)
        
        #self.setWindowIcon(QIcon(ICONO))
        self.setContentsMargins(0, 0, 0, 0)
        self.label.setAttribute(Qt.WA_TranslucentBackground, True)
        self.label_2.setAttribute(Qt.WA_TranslucentBackground, True)
        # -----------------Trigger-----------------
        self.botonRegistro.clicked.connect(self.validar)
    
    def abrirLogin(self):
        self.switch_Login.emit()
    
    def getUsuario(self):
        return self.lineEditUsuario.text()
    
    def getContrasena(self):
        return self.lineEditContrasena.text()
    
    def getContrasena2(self):
        return self.lineEditContrasena2.text()

    def validar(self):
        self.sigValidar.emit()



 
        