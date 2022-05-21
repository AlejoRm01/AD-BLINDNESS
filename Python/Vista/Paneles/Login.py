import sys
from UI.UI_Login import *
from Utiles.DB_Driver import getUsuario
#from Constantes import ADMINISTRADOR, CORREO
class Login():
    
    def __init__(self):
        self.UIl = UI_login()
        self.usuario = None
        self.contrasena = None

        self.UIl.sigValidar.connect(self.validar)

    def validar(self):
        self.usuario = self.UIl.getUsuario()
        self.contrasena = self.UIl.getContrasena()

        aux = getUsuario(self.usuario)

        if aux == None:
            self.UIl.label_4.setText("El usuario no existe")
            self.UIl.label_4.show()
        elif aux == self.contrasena:
            self.UIl.abrirMenu()
            self.UIl.close()

        
    def show(self):
        self.UIl.show()
        
    def close(self):
        self.UIl.close()
        
    