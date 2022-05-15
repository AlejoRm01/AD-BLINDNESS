from PyQt5.uic import loadUi
from PyQt5 import QtCore, Qt, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from Constantes import *

class UI_login(QMainWindow):
    
    switch_Registro = QtCore.pyqtSignal()
    switch_Menu = QtCore.pyqtSignal()
    switch_Verficar = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super(UI_login, self).__init__()
        loadUi('UI/templates/Login.ui', self)
        
        #self.setWindowIcon(QIcon(ICONO))
        self.setContentsMargins(0, 0, 0, 0)
        self.label.setAttribute(Qt.WA_TranslucentBackground, True)
        self.label_2.setAttribute(Qt.WA_TranslucentBackground, True)
        # -----------------Trigger-----------------
        self.botonIngresar.clicked.connect(self.abrirMenu)
        self.botonRegistro.clicked.connect(self.abrirRegistro)
        
    def abrirRegistro(self):
        self.switch_Registro.emit()
        
    def validar(self):
        self.sigValidar.emit()  
        
    def abrirMenu(self):
        self.switch_Menu.emit()