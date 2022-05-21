import sys
from UI.UI_SignUp import *
from Utiles.DB_Driver import agregarUs, getUsuario
from Utiles.Correo import enviarCorreo

class SignUp():
    
    def __init__(self):
        self.UIs = UI_SignUp()
        self.usuario = None
        self.contrasena = None
        self.contrasena2 = None


        self.UIs.sigValidar.connect(self.get_userInfo)
    
    def get_userInfo(self):
        self.usuario = self.UIs.getUsuario()
        self.contrasena = self.UIs.getContrasena()
        self.contrasena2 = self.UIs.getContrasena2()
        
        if self.contrasena != self.contrasena2:
            self.UIs.label_4.setText("Las contraseñas no coinciden")
            self.UIs.label_4.show()
        else:
            self.UIs.label_4.hide()
            self.UIs.label_4.setText("")
            self.crear(self.usuario, self.contrasena)
            enviarCorreo(self.usuario)
            self.UIs.label_4.setText("Se ha enviado un correo a su cuenta de correo electronico")
            self.UIs.label_4.show()
            self.UIs.close()

    def crear(self, usuario, contrasena):
        if getUsuario(usuario) == None:
            agregarUs(usuario, contrasena)
        else:
            self.UIs.label_4.setText("El usuario ya existe")
            self.UIs.label_4.show()


    def show(self):
        self.UIs.show()
        
    def close(self):
        self.UIs.close()