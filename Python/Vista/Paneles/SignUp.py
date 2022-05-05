import sys
#from Utiles.Verificar import verificar
from UI.UI_SignUp import *
#from Utiles.EnviarCorreo import enviarCorreo
#from Constantes import ADMINISTRADOR, CORREO
class SignUp():
    
    def __init__(self):
        self.UIs = UI_SignUp()
        self.usuario = None
        self.contrasena = None
        
    def validar(self):
        pass
    
    def show(self):
        self.UIs.show()
        
    def close(self):
        self.UIs.close()