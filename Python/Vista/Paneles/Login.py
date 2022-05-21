import sys
#from Utiles.Verificar import verificar
from UI.UI_Login import *
#from Utiles.EnviarCorreo import enviarCorreo
#from Constantes import ADMINISTRADOR, CORREO
class Login():
    
    def __init__(self):
        self.UIl = UI_login()
        self.usuario = None
        self.contrasena = None


    def validar(self):
        self.usuario = self.UIl.getUsuario()
        self.contrasena = self.UIl.getContrasena()
        
    
    def show(self):
        self.UIl.show()
        
    def close(self):
        self.UIl.close()
        
    